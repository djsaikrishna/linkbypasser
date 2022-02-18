from os import environ

import asyncio
import re
from pyrogram import Client, filters
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse



API_ID = 6230820
API_HASH = "4c9af8bc82ea492153ba5eae99b25582"
BOT_TOKEN = "1922165225:AAGsx08SWUkWDU9GqwwXF5RfEXfehKYuLd4"
LOG_CHANNEL = -1001319180704

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
async def sendFile(update,context):
    try: 	
        await update.message.reply_document(update.message.document.file_id) 

    except Exception as e: 	
        await update.message.reply_text(e)


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private) 
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    supported = ["gplinks","droplink"]
    if "gplinks" in link : 
        try:
            k = await message.reply(f"**Please Wait , Bot Is processing The Link {message.text}**")
            bypass_link = await gplinks_bypass(link) 
            link_by = bypass_link.get('url')
          
            
            
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'            
            await message.reply(txt, quote = True)
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
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
            await message.reply(txt, quote = True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)
    if 'gplinks' not in link and 'droplink' not in link:
        try:
            txt1 = f'**{message.text} \n {message.chat.username} / {message.chat.id} \n My Bot Support Only Gplinks , Droplink .So Dont Use Any Other Link To Spam The Bot** \n\n **Any Issued Contact @LoveToRide**'
            await message.reply(txt1 , quote = True) 
            await bot.send_message(LOG_CHANNEL, txt1)
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)                    
async def gplinks_bypass(url):
    client = requests.Session()
    res = client.get(url)
    
    h = { "referer": res.url }
    res = client.get(url, headers=h)
    
    bs4 = BeautifulSoup(res.content, 'lxml')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    time.sleep(10) # !important
    
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'
    res = client.post(final_url, data=data, headers=h).json()

    return res

async def droplink_bypass(url):
    client = requests.Session()
    res = client.get(url)

    ref = re.findall("action[ ]{0,}=[ ]{0,}['|\"](.*?)['|\"]", res.text)[0]

    h = {'referer': ref}
    res = client.get(url, headers=h)

    bs4 = BeautifulSoup(res.content, 'lxml')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    time.sleep(3.1)
    res = client.post(final_url, data=data, headers=h).json()

    return res


bot.run()
