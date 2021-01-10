import aiohttp
import asyncio
import datetime
import time

def time_display():
  dt_now = datetime.datetime.now()
  return dt_now.strftime('[%H:%M:%S]')
async def post(URL):
  print(f'{time_display()} 送信中｜{URL}')
  async with aiohttp.ClientSession() as session:
    async with session.post(URL) as resp:
      print(f'{time_display()} 完了  ｜{URL}')
      
async def postlist():
  #await post("https://post.hrtk92.repl.co/")
  await post("https://web.hrtk92.repl.co/")
  await post("https://fortnite-lobbybot.hrsnow.repl.co/")
  
while True:
    time.sleep(1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(postlist())