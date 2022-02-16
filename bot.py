from os import environ
import aiohttp
from pyrogram import Client, filters
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse



API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', '5fd20df0c4db85798dd4f5ff3d03e3606a94f98b')

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**𝗛𝗘𝗟𝗟𝗢🎈{message.chat.first_name}!**\n\n"
        "𝗜'𝗺 𝗚𝗣𝗹𝗶𝗻𝗸 𝗯𝗼𝘁. 𝗝𝘂𝘀𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗹𝗶𝗻𝗸 𝗮𝗻𝗱 𝗴𝗲𝘁 𝗦𝗵𝗼𝗿𝘁𝗲𝗻𝗲𝗱 𝗨𝗥𝗟. \n\n 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗕𝘆 @CyberBoyAyush💖")


@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private) 
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        bypass_link =  gplinks_bypass(link) 
        link_by = bypass_link.get('url')
        
        await message.reply(f'Here is your {link_by}')
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
                            
def gplinks_bypass(url):
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


bot.run()
