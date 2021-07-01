from telethon import events, Button 
from Rimuru import rimuru 
from pytube import *
import os

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^!s(.*)'))
async def songs(slime):
  args = slime.message.text[2:]
  await slime.delete()
  yt = YouTube(args)
  ytu = yt.streams.get_audio_only()
  dl = ytu.download()
  path, ext = os.path.splitext(dl)
  file_name = path + ".mp3"
  dl = os.rename(dl, file_name)
  await rimuru.send_file(slime.chat_id, file=open(file_name, 'rb'))
  os.remove(file_name)
