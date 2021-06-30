import os 
from telethon.sync import TelegramClient 
from telethon.sessions import StringSession 

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
string_one = os.environ.get('SESSION_ONE')
bot_token = os.environ.get('BOT_TOKEN')
pm_log = int(os.environ.get('PM_LOG'))
tag_log = int(os.environ.get('TAG_LOG'))
db_uri = os.environ.get('DATABASE_URL')

def mention(name, userid):
  return f"[{name}]({userid})"


rimuru = TelegramClient(StringSession(string_one), api_id, api_hash)
rafael = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
