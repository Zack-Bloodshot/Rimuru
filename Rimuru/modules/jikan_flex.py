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
  text = f'**{get[0]} on MyAnimeList**[­]({get[2]})\n\n**Anime Statistics:**\n\t\t**Watching:** {get[5]}\n\t\t**Completed:** {get[6]}\n\t\t**Total Entries:** {get[7]}\n\t\t**Episodes watched:** {get[8]}\n\n**Mangas Stats:**\n\t\t**Reading :** {get[11]}\n\t\t**Completed:** {get[12]}\n\t\t**Total Entries:** {get[13]}\n\t\t**Chapters Read:** {get[14]}\n'
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
  
  