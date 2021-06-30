from Rimuru import rimuru, rafael, mention
from telethon import events, Button
import time

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#(alive)'))
async def alive(slime):
  me = await rimuru.get_me()
  kek = mention(me.first_name, me.id)
  await slime.edit(f"「Yos, Great Sage on!」\nMaster: {kek}")
  
@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ping'))
async def ping(slime):
  start = time.time()
  await slime.edit("`۞pinging....`")
  end = time.time()
  pon = (start - end).microseconds / 100
  await slime.edit(f"ᑭOᑎᘜ!!\n\npong time: {pon}ms")

@rafael.on(events.NewMessage(outgoing=True,pattern=r'^/start'))
async def start(slime):
  await slime.reply("Im up!")
  