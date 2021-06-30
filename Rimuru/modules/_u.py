from Rimuru import rimuru, rafael, mention
from telethon import events, Button
import time

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#(alive)'))
async def alive(slime):
  me = await rimuru.get_me()
  kek = mention(me.first_name, me.id)
  slime.edit(f"*「Yos, Great Sage on!」*\n\nOwner: *{kek}*")
  
@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ping'))
async def ping(slime):
  start = time.time()
  slime.edit("`۞pinging....`")
  end = time.time()
  pon = (start - end).microseconds / 100
  slime.edit(f"ᑭOᑎᘜ!!\n\npong time: {pon}ms")

@rafael.on(events.NewMessage(outgoing=True,pattern=r'^/start'))
async def start(slime):
  slime.reply("Im up!")
  