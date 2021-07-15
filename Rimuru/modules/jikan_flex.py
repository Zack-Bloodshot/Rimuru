from jikanpy import Jikan
import jikanpy.exceptions
from Rimuru import rimuru, rafael
from telethon import events, Button

class flex_jikan:
  def __init__(self, username):
    self.username = username 
    
  def flex(username):
    jikan = Jikan()
    try:
      hek = jikan.user(username=username, request='profile')
    except jikanpy.exceptions.APIException:
      return False
    anis = hek.get('anime_stats')
    mangs = hek.get('manga_stats')
    result = [
      hek.get('username'),
      hek.get('url'),
      hek.get('image_url'),
      anis.get('days_watched'),
      anis.get('mean_score'),
      anis.get('watching'),
      anis.get('completed'),
      anis.get('total_entries'),
      anis.get('episodes_watched'),
      mangs.get('days_read'),
      mangs.get('mean_score'),
      mangs.get('reading'),
      mangs.get('completed'),
      mangs.get('total_entries'),
      mangs.get('chapters_read'),
    ]  
    return result
    
    
@rafael.on(events.InlineQuery)    
async def flexer(slime):
  if slime.text == '':
    await slime.answer([], switch_pm='Search any MAL user.....', switch_pm_param='start')
    return 
  elif slime.text == 'help':
    return
  user = slime.text 
  get = flex_jikan.flex(user)
  if get == False:
    await slime.answer([], switch_pm='User not found....', switch_pm_param='start')
    return
  text = f'**[{get[0]}({get[2]})**\n**Anime Statistics:**\nDays Watched: {get[3]})\nMean Score: {get[4]}\nWatching: {get[5]}\nCompleted: {get[6]}\nTotal Entries: {get[7]}\nEpisodes watched: {get[8]}\n\n**Mangas Stats:**\nDays Read: {get[9]}\nMean Score: {get[10]}\nReading : {get[11]}\nCompleted: {get[12]}\nTotal Entries: {get[13]}\nChapters Read {get[14]}\n'
  hek = [
    slime.builder.article(
      title = f'{get[0]} stats',
      description=text,
      text=text,
      buttons=[
        Button.url(
          text='Profile',
          url=get[2],
          )
        ]
      )
    ]
  await slime.answer(hek)  
  
  