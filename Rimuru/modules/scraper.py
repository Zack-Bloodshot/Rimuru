from telethon import events, Button
from Rimuru import rimuru


@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#s(.*)'))
async def movscrape(slime):
  args = slime.message.text[2:]
  chats = [ -1001335426946, -1001420781438, -1001452018343]
  count = 0
  await slime.edit("Searching....")
  for chat in chats:
    if not count == 0:
      break
    async for msg in rimuru.iter_messages(chat, reverse=True, search=args):
      if msg.video or msg.document:
        await rimuru.send_file(slime.chat.id, msg.media, caption=msg.text)
        count += 1  
  if not count == 0:
    if slime.reply_to_msg_id:
      slime = await slime.get_reply_message()
    else:
      pass 
    await slime.reply("👆") 
    await slime.delete()
  else:
    await slime.edit("Not found....")
    
    

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ani(.*)'))
async def aniscrape(slime):
  args = slime.message.text[4:]
  count = 0
  async for msg in rimuru.iter_messages(-1001231649146, reverse=True, search=args):
    if msg.media:
      await rimuru.send_file(slime.chat_id, file=msg.media, caption=msg.text)
      count += 1
