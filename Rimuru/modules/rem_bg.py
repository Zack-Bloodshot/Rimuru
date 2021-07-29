from rembg.bg import remove
import numpy as np
import io
from PIL import Image
from Rimuru import rimuru, rafael
from telethon import events, Button
import os

@rimuru.on(events.NewMessage(outgoing=True,pattern=r'#srmbg'))
async def rem_bg(slime):
  reply = await slime.get_reply_message()
  dl = await reply.download_media()
  if dl.endswith('jpg'):
    pass
  elif dl.endswith('png'):
    pass 
  else:
    return
  input_path = dl
  output_path = 'out.png'
  f = np.fromfile(input_path)
  result = remove(f)
  img = Image.open(io.BytesIO(result)).convert("RGBA")
  img.save(output_path)
  os.rename('out.png', 'out.wepb')
  await rimuru.send_file(slime.chat_id, file='out.webp')
  os.remove('out.webp')
  os.remove(dl)