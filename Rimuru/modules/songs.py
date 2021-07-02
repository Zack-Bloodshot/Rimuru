from telethon import events, Button 
from Rimuru import rimuru 
import youtube_dl
import logging
import os
from youtube_search import YoutubeSearch

LOGS = logging.getLogger(__name__)

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^!s(.*)'))
async def songs(slime):
  opts = {
    "outtmpl": "%(title)s.%(ext)s",
    "logger": LOGS,
    "writethumbnail": True,
    "prefer_ffmpeg": True,
    "format": "bestaudio/best",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [
      {
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": uid,
      },
      {"key": "EmbedThumbnail"},  # ERROR: Conversion failed!
      {"key": "FFmpegMetadata"},
    ],
    "quiet": True,
  }
  args = slime.message.text[2:]
  if args.startswith("https://"):
    url = args
  else:
    result = YoutubeSearch(args,max_results=1).to_dict()
    url = "https://youtu.be/" + result[0]['id']
  await slime.delete()
  with youtube_dl.YouTubeDL(opts) as ydl:
    dl = ydl.download(url)
  m = await slime.respond("Downloaded, Now uploading....")
  async with rimuru.action(slime.chat_id, 'audio'):
    await rimuru.send_message(slime.chat_id, file=open(dl, 'rb'), force_document=False)
  await m.delete()
  os.remove(file_name)
