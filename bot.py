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
    
    bypass_link =  await lv_bypass(link)
    print(bypass_link)
    
    # this function for #linkvertise
    if "https" in link:
        try:

            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            link = f"{link}"
            bypass_link =  await lv_bypass(link)
            print(bypass_link)
            bypass_link = bypass_link
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{bypass_link}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
            await message.reply(f'{e}', quote=True)

    if "fumacrom" in link:
        try:
            
            link = f"{message.text}"
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link = await adfly_bypass(link)
            bypass_link = bypass_link.get('bypassed_url')
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{bypass_link}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
            
        except Exception as e:
            
            await message.reply(f'{e}', quote=True)
    if "ouo" in link :
         try:
            
            link = f"{message.text}"
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            
            bypass_link = await ouo_bypass(link)
            print(bypass_link)
            bypass_link = bypass_link.get('bypassed_link')
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{bypass_link}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)

         except Exception as e:
            await message.reply(f'{e}', quote=True)
    if "gplinks" in link:
        try:
            k = await message.reply(f"**Please Wait , Bot Is processing The Link {message.text}**")
            bypass_link = await gplinks_bypass(link)
            link_by = bypass_link.get('url')

            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**\nTotal Links = {count}**'
            await message.reply(txt, quote=True)

            await bot.send_message(LOG_CHANNEL, txt)

        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)
            
    if "droplink" in link:
        try:

            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link = await droplink_bypass(link)
            link_by = bypass_link.get('url')

            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)
import re
import time
import json
import base64
import requests

# -------------------------------------------

async def lv_bypass(url):
    client = requests.Session()
    
    headers = {
        "User-Agent": "AppleTV6,2/11.1",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    client.headers.update(headers)
    
    url = url.replace("%3D", " ").replace("&o=sharing", "").replace("?o=sharing", "").replace("dynamic?r=", "dynamic/?r=")
    
    id_name = re.search(r"\/\d+\/[^\/]+", url)
    
    if not id_name: return None
    
    paths = [
        "/captcha", 
        "/countdown_impression?trafficOrigin=network", 
        "/todo_impression?mobile=true&trafficOrigin=network"
    ]
    
    for path in paths:
        url = f"https://publisher.linkvertise.com/api/v1/redirect/link{id_name[0]}{path}"
        response = client.get(url).json()
        if response["success"]: break
    
    data = client.get(f"https://publisher.linkvertise.com/api/v1/redirect/link/static{id_name[0]}").json()

    out = {
        'timestamp':int(str(time.time_ns())[0:13]),
        'random':"6548307", 
        'link_id':data["data"]["link"]["id"]
    }
    
    options = {
        'serial': base64.b64encode(json.dumps(out).encode()).decode()
    }
    
    data = client.get("https://publisher.linkvertise.com/api/v1/account").json()
    user_token = data["user_token"] if "user_token" in data.keys() else None
    
    url_submit = f"https://publisher.linkvertise.com/api/v1/redirect/link{id_name[0]}/target?X-Linkvertise-UT={user_token}"
    
    data = client.post(url_submit, json=options).json()
    
    return data

# -------------------------------------------

      
    
bot.run()

