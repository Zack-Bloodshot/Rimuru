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
      str(hek.get('username')),
      str(hek.get('url')),
      str(hek.get('image_url')),
      str(anis.get('days_watched')),
      str(anis.get('mean_score')),
      str(anis.get('watching')),
      str(anis.get('completed')),
      str(anis.get('total_entries')),
      str(anis.get('episodes_watched')),
      str(mangs.get('days_read')),
      str(mangs.get('mean_score')),
      str(mangs.get('reading')),
      str(mangs.get('completed')),
      str(mangs.get('total_entries')),
      str(mangs.get('chapters_read')),
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
  text = f'**{get[0]}[­]({get[2]})**\n\n**Anime Statistics:**\n\tDays Watched: {get[3]}\n\tMean Score: {get[4]}\n\yWatching: {get[5]}\n\tCompleted: {get[6]}\n\tTotal Entries: {get[7]}\n\tEpisodes watched: {get[8]}\n\n**Mangas Stats:**\n\tDays Read: {get[9]}\n\tMean Score: {get[10]}\n\tReading : {get[11]}\n\tCompleted: {get[12]}\n\tTotal Entries: {get[13]}\n\tChapters Read {get[14]}\n'
  hek = [
    slime.builder.article(
      title = f'{get[0]} stats',
      description='Anime Stats and manga stats....',
      text=text,
      buttons=[
        Button.url(
          text='Profile',
          url=get[1],
          )
        ]
      )
    ]
  await slime.answer(hek)  
  
  