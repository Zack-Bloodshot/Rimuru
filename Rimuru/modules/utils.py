from Rimuru import rimuru 
from telethon import events, Button
import time 

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^#purge(.*)'))
async def purge(slime):
  msg = slime.message.text.split(" ", 3)
  reply = await slime.get_reply()
  if not reply:
    slime.edit("Reply...")
    time.sleep(1)
    slime.delete()
  from_msg = reply.id
  try:
    to_msg = msg[2]
  except IndexError:
    to_msg = False 
  count = 0
  async for msg in rimuru.iter_messages(slime.chat_id, offset_id=int(from_msg)):
    if not to_msg == False:
      if count == int(to_msg):
        break 
    try:
      await msg.delete()
    except Exception:
      pass
  if not count == 0:
    await slime.respond(f"Purged {count} messages..")