from telethon import events, Button 
from Rimuru import rimuru 
from pytube import *
import os
from youtube_search import YoutubeSearch

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^!s(.*)'))
async def songs(slime):
  args = slime.message.text[2:]
  if args.startswith("https://"):
    url = args
  else:
    result = YoutubeSearch(args,max_results=1).to_dict()
    url = "https://youtu.be/" + results[0]['id']
  await slime.delete()
  yt = YouTube(url)
  ytu = yt.streams.get_audio_only()
  dl = ytu.download()
  path, ext = os.path.splitext(dl)
  file_name = path + ".mp3"
  dl = os.rename(dl, file_name)
  async with rimuru.action(slime.chat_id, 'audio'):
    await rimuru.send_file(slime.chat_id, file=open(file_name, 'rb'), force_document=False)
  os.remove(file_name)
