from Rimuru import rimuru, rafael, pm_log, tag_log, mention
from telethon import events, Buttons, functions, types
from Rimuru.modules.sql import pm_sql as pm
import time

now = {}


@rimuru.on(events.NewMessage(incoming=True))
async def pmperm(slime):
  if not slime.is_private:
    return
  user = slime.sender
  name = f"{user.first_name} {user.last_name}"
  men = mention(name, user.id)
  await rafael.send_message(pm_log, f"*{men}*: {slime.message.text}")
  if pm.is_approved(user.id):
    return 
  if user.id in now:
    count = now[user.id] 
    if count == 10:
      await slime.rimuru.send_file(file="CAADBQADmwIAAjYOMFfXvrzk6UlajwI")
      await slime.reply("Stop now, or i will block you...")
    elif count == 11:
      await rimuru(functions.contacts.BlockRequest(id=user.id))
      await rimuru.send_message(slime.chat_id, "Agh, You wont lose your virginity here...")
      await rimuru.send_message(slime.chat_id, "Wait till Abhi comes..")
    else:
      now[user.id] = count + 1
  else:
    now[user.id] = 0 
    await rimuru.send_file(file="CAACAgUAAxkBAAFEmXxg2wLMk1JJ4D3hDPANaCzUR5V6mQACWgIAAo-r2FTHhGRff7EgdSAE")
    await slime.reply("Yo! Please wait till Abhi come's and approves you...")


@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(a|approve)"))    
def approve(slime):
  if not slime.is_private:
    return 
  slime.edit("✿Approving...")
  h = pm.approve(slime.sender_id)
  if h == False:
    slime.edit("⍟Already aprovved..")
    time.sleep(1)
    slime.delete()
    return
  slime.edit("✧Successful!")
  time.sleep(1)
  slime.delete()

@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(d|disapprove)"))    
def approve(slime):
  if not slime.is_private:
    return 
  slime.edit("✿Disapproving...")
  h = pm.disapprove(slime.sender_id)
  if h == False:
    slime.edit("⍟Already disaprovved..")
    time.sleep(1)
    slime.delete()
    return
  slime.edit("✧Successful!")
  time.sleep(1)
  slime.delete()
