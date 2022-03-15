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

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL'))

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
        if 'MB' in link_te or 'GB' in link_te:
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
    for last_check,last_text in zip(getting_filter , getting_text):

        get_c = get_c+last_text+'\n\n'

      
        if 'www' in last_check:
            
            get_c = get_c + last_check +'\n\n'
            

        

        elif 'applications' in last_check:
            
            get_c = get_c + last_check +'\n\n'
    await message.reply(get_c, quote=True)

            
       
                
bot.run()
