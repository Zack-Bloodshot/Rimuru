from telethon import events, Buttons 
from Rimuru import rimuru


@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#s(.*)'))
async def movscrape(slime):
  args = slime.message.text[2:]
  chats = [-1001420781438, -1001335426946, -1001452018343]
  count = 0
  for chat in chats:
    if not count == 0:
      break
    async for msg in rimuru.iter_messages(chat, query=args):
      if msg.media
        await rimuru.send_file(slime.chat.id, msg.media, caption=msg.caption)
        count += 1  
  if not count == 0:
    if slime.reply_to_msg_id:
      slime = await slime.get_reply()
    else:
      pass 
    slime.reply("👆")
    
    

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ani(.*)'))
async def aniscrape(slime):
  args = slime.message.text[4:]
  count = 0
  async for msg in rimuru.iter_messages(-1001231649146, search=args):
    if msg.media:
      await rimuru.send_file(slime.chat_id, file=msg.media, caption=msg.caption)
      count += 1