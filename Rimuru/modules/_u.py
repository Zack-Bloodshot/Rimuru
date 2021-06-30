from Rimuru import rimuru, rafael, mention
from telethon import events, Button
from datetime import datetime as dt

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#(alive)'))
async def alive(slime):
  me = await rimuru.get_me()
  kek = mention(me.first_name, me.id)
  await slime.edit(f"「Yos, Great Sage on!」\nMaster: {kek}")
  
@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ping'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`۞pinging....`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f"ᑭOᑎᘜ!!\n\npong time: {pon}ms")

@rafael.on(events.NewMessage(outgoing=True,pattern=r'^/start'))
async def start(slime):
  await slime.reply("Im up!")
  