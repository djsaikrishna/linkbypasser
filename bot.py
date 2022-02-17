from os import environ
import aiohttp
import asyncio
import re
from pyrogram import Client, filters
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse



API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hey {message.chat.first_name}!**\n\n"
        "Hey I Am GPlink By_Passer Don't Flood A Bot ")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private) 
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    supported = ["gplinks","droplink"]
    if "gplinks" in link : 
        try:
            bypass_link = await gplinks_bypass(link) 
            link_by = bypass_link.get('url')
            k = await message.reply(f"**Please Wait , Bot Is Processing The Link**")
            await asyncio.sleep(9)
            await k.delete()
            await message.reply(f' **Here is your** : </b> \n\n {link_by}')
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)
    if "droplink" in link:
        try:
            bypass_link = await droplink_bypass(link) 
            link_by = bypass_link.get('url')
            k = await message.reply(f"**Please Wait , Bot Is Processing The Link**")
            await asyncio.sleep(9)
            await k.delete()
            await message.reply(f' **Here is your** : </b> \n\n {link_by}')
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)
    if supported not in link:
        await message.reply(f'**My Bot Support Only Gplinks , Droplink .So Dont Use Any Other Link To Spam The Bot**') 
                                
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
