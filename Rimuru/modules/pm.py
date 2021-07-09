from Rimuru import rimuru, rafael, pm_log, tag_log, mention
from telethon import events, Button, functions, types
from Rimuru.modules.sql import pm_sql as pm
import time

now = {}
rafael.parse_mode='md'

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
    await rafael.send_message(pm_log, f"**{user.first_name}**: {slime.message.text}")
  else:
    await rafael.send_file(pm_log, file=slime.media, caption=f"{user.first_name}: {slime.message.text}")
  if pm.is_approved(user.id):
    return 
  if user.id in now:
    count = now[user.id] 
    if count == 5:
      await rimuru.send_file(slime.chat_id,file="CAADBQADUgMAAp6ZWVadu3NWvPQb8gI")
      time.sleep(2)
      await slime.reply("Stop now, or i will block you...")
      now[user.id] = count + 1
    elif count == 6:
      await rimuru(functions.contacts.BlockRequest(id=user.id))
      await rimuru.send_message(slime.chat_id, "Agh, You wont lose your virginity here...")
      time.sleep(2)
      await rimuru.send_message(slime.chat_id, "Wait till Abhi comes..")
    else:
      now[user.id] = count + 1
  else:
    now[user.id] = 1


@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(a|approve)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Approving...")
  user = await slime.get_chat()
  h = pm.approve(user.id)
  if h == False:
    await slime.edit("⍟Already aprovved..")
    time.sleep(1)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(1)
  await slime.delete()

@rimuru.on(events.NewMessage(outgoing=True, pattern=r"^#(d|disapprove)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Disapproving...")
  user = await slime.get_chat()
  h = pm.disapprove(user.id)
  if h == False:
    await slime.edit("⍟Already disaprovved..")
    time.sleep(1)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(1)
  await slime.delete()
