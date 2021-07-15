from Rimuru import rimuru, rafael, mention, alive_pic, help_strings
from telethon import events, Button
from datetime import datetime as dt

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#(alive)'))
async def alive(slime):
  me = await rimuru.get_me()
  date = dt.now()
  date = date.strftime("%B %d, %Y")
  kek = mention(me.first_name, me.id)
  await slime.edit(f"「 **Great Sage On!** 」\n**Date:** `{date}`[­ ]({alive_pic})\n**Master:** {kek}", link_preview=True)
  
@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#ping$'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`۞pinging....`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f"ᑭOᑎᘜ!!\n\npong time: {pon}ms")

@rafael.on(events.NewMessage(outgoing=True,pattern=r'^/start'))
async def start(slime):
  await slime.reply("Im up!")
  
@rafael.on(events.InlineQuery(pattern=r'help'))
async def helppp(slime):
  builder = slime.builder 
  h = [
    builder.article(
    title='Help',
    text='Press button, to see help',
    buttons=[
      Button.inline(
        text='Help',
        data='help'
        )
      ]
  )
  ]
  await slime.answer(h)

@rafael.on(events.CallbackQuery(pattern=b'help'))
async def helpcall(slime):
  await slime.answer(help_strings, alert=True)
  
  
@rimuru.on(events.NewMessage(outgoing=True,pattern=r'^#help$'))  
async def helpp(slime):
  great_sage = rafael.me.username
  results = await ultroid_bot.inline_query(great_sage, "help") 
  await results[0].click(slime.chat_id, reply_to=ult.reply_to_msg_id, hide_via=True) 