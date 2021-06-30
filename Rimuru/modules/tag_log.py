from telethon import events, Button, functions, types  
from Rimuru import rimuru, rafael, tag_log, mention


@rimuru.on(events.NewMessage(incoming=True, func=lambda e: (e.mentioned)))
async def taglog(slime):
  user = slime.sender 
  if user.bot:
    return 
  kek = mention(f"{user.first_name} {user.last_name}", user.id)
  chat = slime.chat
  msg = slime.message
  if msg.text:
    link = f"https://t.me/{chat.id}/{msg.id}"
    text = f"*{kek}* in *{chat.title}*\n\n`{msg.text}`"
    await rafael.send_message(tag_log, text, buttons= [Button.url(text="Message", url = link)])
  else:
    return
  