from Rimuru import rimuru 
from telethon import events, Button
import time 

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^#purge(.*)'))
async def purge(slime):
  msg = slime.message.text.split(" ", 3)
  reply = await slime.get_reply_message()
  if not reply:
    await slime.edit("Reply...")
    time.sleep(1)
    await slime.delete()
  from_msg = reply.id - 1
  try:
    to_msg = msg[2]
  except IndexError:
    to_msg = False 
  count = 0
  async for msg in rimuru.iter_messages(slime.chat_id, reverse=True, offset_id=from_msg):
    if not to_msg == False:
      if count == int(to_msg):
        break 
    try:
      await msg.delete()
      count += 1
    except Exception:
      pass
  if not count == 0:
    await slime.respond(f"Purged {count} messages..")
    
@rimuru.on(event.NewMessage(outgoing=True, pattern=r'^#id'))    
async def idscrape(slime):
    if slime.reply_to_msg_id:
        await slime.get_input_chat()
        r_msg = await slime.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await slime.edit("**Current Chat ID:**  `{}`\n**From User ID:**  `{}`\n**Bot API File ID:**  `{}`".format(str(event.chat_id),str(r_msg.sender_id),bot_api_file_id))
        else:
            await slime.edit("**Chat ID:**  `{}`\n**User ID:**  `{}`".format(str(event.chat_id),str(r_msg.sender_id)))
    elif event.pattern_match.group(1):
        ids = await get_user_id(event.pattern_match.group(1))
        await slime.edit("**Chat ID:**  `{}`\n**User ID:**  `{}`".format(str(event.chat_id),str(ids)))
    else:
        await slime.edit("**Current Chat ID:**  `{}`".format(str(event.chat_id)))
    