from os import environ

import asyncio
import re
from pyrogram import Client, filters
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#requirements 

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
LOG_CHANNEL = environ.get('LOG_CHANNEL')
group_log = environ.get('group_log')
USER_STRING_SESSION = environ.get('USER_STRING_SESSION')
rss_session =  Client(USER_STRING_SESSION, api_id=API_ID, api_hash=API_HASH)
rss_session.start()


#modified code

bot = Client('gplink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)
## install before run
# apt-get -y install python3-pip
# apt-get install python3-bs4
# pip3 install requests
# pip3 install BeautifulSoup4 
# pip3 install clint
# pip3 install -U gazpacho


import os
import requests
from bs4 import BeautifulSoup
from gazpacho import get,Soup
from clint.textui import progress
import argparse
from lxml import html
import urllib

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    supported = ["gplinks", "droplink"]
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

    if "linkvertise" in link :
        try:
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link = await lv_bypass(link)
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{bypass_link}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**'
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

    if link:
        try:
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link = await adfly_bypass(link)
            link_by = bypass_link.get('bypassed_url')
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
             await message.reply(f'Error: {e}', quote=True)
    if "ouo" in link:
        try:
            k = await message.reply(f"**Please Wait , Bot Is Processing 🔑 The Link {message.text}**")
            bypass_link = await ouo_bypass(link)
            link_by = bypass_link.get('bypassed_link')
            await asyncio.sleep(9)
            await k.delete()
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**'
            await message.reply(txt, quote=True)
            await bot.send_message(LOG_CHANNEL, txt)
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)


    if 'gplinks' not in link and 'droplink' not in link :
        try:
            txt1 = f'**{message.text} \n {message.chat.username} / {message.chat.id} \n My Bot Support Only Gplinks , Droplink .So Dont Use Any Other Link To Spam The Bot** \n\n **Any Issued Contact @LoveToRide**'
            await message.reply(txt1, quote=True)
            await bot.send_message(LOG_CHANNEL, txt1)
        except Exception as e:
            await message.reply(f'Error: {e}', quote=True)



async def gplinks_bypass(url):
    client = requests.Session()
    res = client.get(url)

    h = {"referer": res.url}
    res = client.get(url, headers=h)

    bs4 = BeautifulSoup(res.content, 'lxml')
    inputs = bs4.find_all('input')
    data = {input.get('name'): input.get('value') for input in inputs}

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }

    time.sleep(10)  # !important

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
    data = {input.get('name'): input.get('value') for input in inputs}

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    time.sleep(3.1)
    res = client.post(final_url, data=data, headers=h).json()

    return res

# -------------------------------------------
import re
import time
import json
import base64
import requests
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

    return data["data"]["target"]


import re
import requests
from base64 import b64decode
from urllib.parse import unquote


def decrypt_url(code):
    a, b = '', ''
    for i in range(0, len(code)):
        if i % 2 == 0:
            a += code[i]
        else:
            b = code[i] + b

    key = list(a + b)
    i = 0

    while i < len(key):
        if key[i].isdigit():
            for j in range(i + 1, len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10: key[i] = str(u)
                    i = j
                    break
        i += 1

    key = ''.join(key)
    decrypted = b64decode(key)[16:-16]

    return decrypted.decode('utf-8')


# ==========================================
import re
import requests
from base64 import b64decode
from urllib.parse import unquote
async def adfly_bypass(url):
    res = requests.get(url).text

    out = {'error': False, 'src_url': url}

    try:
        ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        out['error'] = True
        return out

    url = decrypt_url(ysmm)

    if re.search(r'go\.php\?u\=', url):
        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
    elif '&dest=' in url:
        url = unquote(re.sub(r'(.*?)dest=', '', url))

    out['bypassed_url'] = url

    return out


bot.run()

