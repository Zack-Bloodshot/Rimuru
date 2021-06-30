from Rimuru import rimuru, rafael, pm_log, tag_log, mention
from telethon import events, Button, functions, types
from Rimuru.modules.sql import pm_sql as pm
import time

now = {}


@rimuru.on(events.NewMessage(incoming=True))
async def pmperm(slime):
  global now
  if not slime.is_private:
    return
  user = await slime.get_chat()
  if user.bot:
    return
  name = mention(user.first_name, user.id)
  if not slime.media:
    await rafael.send_message(pm_log, f"{name}: {slime.message.text}", parse_mode='md')
  if pm.is_approved(user.id) == False:
    return 
  if user.id in now:
    count = now[user.id] 
    if count == 5:
      await rimuru.send_file(slime.chat_id,file="CAADBQADUgMAAp6ZWVadu3NWvPQb8gI")
      await slime.reply("Stop now, or i will block you...")
      now[user.id] = count + 1
    elif count == 6:
      await rimuru(functions.contacts.BlockRequest(id=user.id))
      await rimuru.send_message(slime.chat_id, "Agh, You wont lose your virginity here...")
      await rimuru.send_message(slime.chat_id, "Wait till Abhi comes..")
    else:
      now[user.id] = count + 1
  else:
    now[user.id] = 1
    await rimuru.send_file(slime.chat_id, file="CAADBQADWgIAAo-r2FTHhGRff7EgdQI")
    await slime.reply("Yo! Please wait till Abhi come's and approves you...")


@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(a|approve)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Approving...")
  h = pm.approve(slime.sender_id)
  if h == False:
    await slime.edit("⍟Already aprovved..")
    time.sleep(1)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(1)
  await slime.delete()

@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(d|disapprove)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Disapproving...")
  h = pm.disapprove(slime.sender_id)
  if h == False:
    await slime.edit("⍟Already disaprovved..")
    time.sleep(1)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(1)
  await slime.delete()
