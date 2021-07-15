import os 
from telethon.sync import TelegramClient 
from telethon.sessions import StringSession 

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_one = os.environ.get('STRING_SESSION')
bot_token = os.environ.get('BOT_TOKEN')
pm_log = int(os.environ.get('PM_LOG'))
tag_log = int(os.environ.get('TAG_LOG'))
db_uri = os.environ.get('DATABASE_URL')
alive_pic = os.environ.get('ALIVE_PIC') 

help_strings = """
`#alive` - Alive?
`#ping` - Pong! kek!
`#a`|`#da`|`#approve`|`#disapprove` - Good ol' pmpermit..., the bot only starts replying on the 5th message and then blocks on the 7th message.
`#s` - scrape movies from three channels kek!
`!s` - Youtube audio downloader, not the best quality tho 
`#id` - reply to anything to id! 
"""

def mention(name, userid):
  return f"[{name}](tg://user?id={userid})"


rimuru = TelegramClient(StringSession(string_one), api_id, api_hash)
rafael = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
