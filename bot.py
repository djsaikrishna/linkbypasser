
from os import environ
import asyncio
import re
import requests

from bs4 import BeautifulSoup

from pyrogram import Client, filters
import time
from adfly import *
from linkvertise import *
from ouo import *
from droplink import *
from gplink import *

API_ID = 6230820
API_HASH = '4c9af8bc82ea492153ba5eae99b25582'
BOT_TOKEN = '1861652521:AAHsirFvvZD0bTwkYgXC_vK3KiMv4WVHMSE'

USER_STRING_SESSION = 'BQAA0OS9l042jAkUkf_SB2PdboiU15xiRFw1w-NmT6PBccxqWqWdv8Ep4l_cvvye2oSX_i7TwoWSpvX4pnyTJTlwjphySt53CXsVp8WR3fG4pQTo18fAvOFMpLVip_0FFqIMvT4bK7NVNo3x-uLjbK9ekwDJzKtLadfOPyIdfotB05cZhjfeB6QY0uc3pTJgrSl6m3v1YTkeMZRuAeHUk-jmqhVJ7orcKkMqNgKwLdfQtwJNHmeS9KkFbNe29E9Dj1mu0qnTlGDGmkKRcIwGBy1or61-qqXWwbk_d4Py8cb95wVO_QuyB8wHrvk5qhrbFgyl0HGMmfuUjFdREYV0caulAAAAATj9R-8A'
rss_session = Client(USER_STRING_SESSION, api_id=int(API_ID), api_hash=API_HASH)

RSS_CHAT_ID = int(-1001592086289)
bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)



@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hai Nanba  {message.chat.first_name}!**\n\n"
        "**Hey I Am By_Passer Bot Don't Flood A Bot ,Don't Use This Bot Without Getting Permission From Developer**.\n\n **Credits : XCSCXR For His Script**   \n\n **Dev By : @LoveToRide**  ")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    link = f"{message.text}"
    k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
    URL = link
    getting_info = requests.get(URL)

    getting_info = getting_info.text

    soup = BeautifulSoup(getting_info,'html.parser')
    text_get = soup.text
    getting_link = []
    getting_text = []
    for link in soup.find_all('a'):
        link_te = link.text
        list1 = link.get('href')
        getting_link.append(list1)
        if link_te.endswith('torrent'):
           getting_text.append(link_te)
        
        
        
     
            

    getting_filter = []
    for dump in getting_link:
        if 'applications' in getting_filter:
            print(f"{last_check}")
        if dump is None :
            pass
        elif 'applications'in dump:
            getting_filter.append(dump)
        elif dump.startswith('www'):
            getting_filter.append(dump)
    get_c = ' '
    get_dat1 = ' '  
    for last_check,last_text in zip(getting_filter , getting_text):

        get_c = get_c+last_text+'\n\n'

      
        if 'www' in last_check:
            
            get_dat1 = get_dat1 +'/mirror '  + last_check +'\n\n'
            

        

        elif 'applications' in last_check:
            
            get_c = get_c +'/mirror ' +  last_check +'\n\n'
               
        print(get_dat1)
       
        await bot.send_message(message.chat.id , text = get_dat1)

    #await message.reply(get_c, quote=True)
    #await rss_session.send_message(RSS_CHAT_ID, text = get_c)

            
       
                
bot.run()
rss_session.start()
