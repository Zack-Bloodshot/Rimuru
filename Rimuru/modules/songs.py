from telethon import events, Button 
from Rimuru import rimuru 
from pytube import *
import os

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^!s(.*)'))
async def songs(slime):
  args = slime.message.text[2:]
  await slime.delete()
  yt = Youtube(args)
  yt = yt.streams.get_only_audio(mp3)
  dl = yt.download()
  await rimuru.send_file(slime.chat_id, file=dl)
  os.remove(dl)
