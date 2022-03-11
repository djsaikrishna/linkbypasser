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
    r = requests.get(URL)

    r = r.text

    soup = BeautifulSoup(r,'html.parser')

    tr = []
    for link in soup.find_all('a'):
        list1 = link.get('href')
        tr.append(list1)


    b = []
    for i in tr:

        if i is None :

           pass
        else:
            b.append(i)
    for ge in b:

        if 'applications' in ge:
            zap = f"Torrent File Link :\n\n {ge}"
            await message.reply(zap, quote=True)
        elif 'magnet' in ge:
            sap = f"Magnetic Link :\n\n {ge}"
            await message.reply(zap, quote=True)
            
            
bot.run()
