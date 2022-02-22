from os import environ
import asyncio
import re
from pyrogram import Client, filters
import time
from adfly import *
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
    
    # this function for #linkvertise
    if "linkvertise" in link:
        try:

            link = f"{message.text}"
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link =  lv_bypass(link)
            bypass_link = bypass_link
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{bypass_link}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
            await message.reply(f'{e}', quote=True)

   
bot.run()
