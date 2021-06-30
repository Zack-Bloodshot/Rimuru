from Rimuru import rimuru 
from telethon import events, Buttons 

ONECHAIN = False

@rimuru.on(events.NewMessage(outgoing=True, pattern=r'^#onechain')) 
async def onechain(slime):
  if ONECHAIN == True:
    slime.delete()
  else:
    ONECHAIN = True
    slime.delete()
    
@rimuru.on(events.NewMessage(outgoing=True, pattern=r'Turn(.*)'))
async def one(slime):
  if not slime.sender_id == 840338206:
    return 
  msg = slime.split(" ")
  me = await rimuru.get_me()
  if not msg[1] == me.first_name:
    return 
  word = msg[9]
  letters = msg[14]