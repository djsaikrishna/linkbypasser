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


# default var
home_url= 'http://tamilyogi.best/category/tamilyogi-full-movie-online/'

# get optional arguments
parser = argparse.ArgumentParser()
parser.add_argument('-path', type = str, default='/app/.heroku/python/lib/python3.7')
parser.add_argument('-number', type=int, default=1)
parser.add_argument('-tmp_path', type=str, default='/app/.heroku/python/lib/python3.7/')
args = parser.parse_args()

number_of_videos = args.number
download_link_path = args.path
tmp_path = args.tmp_path + '\dawnloaded_list.txt' 
# 1.Get file names from directory
def file_list():
    file_names=os.listdir(download_link_path)
    return file_names

# Split and get text between two substring
# TODO may be can use json format to split inseast the function
def ind(begining, end, contenent):
    idx_begining = contenent.index(begining)
    idx_end = contenent.index(end)

    res = ''
    for idx in range(idx_begining + len(begining) + 1, idx_end):
        res = res + contenent[idx]
    #print("The extracted string : \n" + res,"\n")
    return res

# Download the  video
def download_file(url, path, title):
    filename = path + "/" + title + ".mp4"
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        total_length = r.headers.get('content-length')
        print("Downloading Movie:", title)
        #print(total_length, url, path, title)
        # for print a progress bar during the dawnload
        for chunk in progress.bar(r.iter_content(chunk_size=1024),\
            expected_size=(int(total_length)/1024) + 1): 
             if chunk: # filter out keep-alive new chunks
                f.write(chunk)    
                f.flush()
        print ("Downloading Done\n")
        f.close()

# Get request contenent
page = requests.get(home_url)

soup = BeautifulSoup(page.content, 'html.parser')
id_postcontent = soup.find_all(class_='postcontent')

s = 0
titles = []
postcontent_links = []
for id_postcontent in id_postcontent:
    s += 1
    href_line = id_postcontent.find(href=True)
    postcontent_links.append(href_line['href'])
    #titles.append(href_line['title']\
    #   .replace(' ', '_').split("(")[0][:-1])
    titles.append(href_line['title']\
        .replace('- ', '')\
        .replace(' ', '_')\
        .replace(')', '')\
        .replace('(', '')\
        .replace('_Watch_Online', ''))
    if s == number_of_videos:
        break

iframe_src_link = []
for links in postcontent_links:
    page1 = requests.get(links)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    entry= soup1.find(class_='entry')
    iframe_link=entry.iframe.attrs['src']
    iframe_src_link.append(iframe_link)
    #print("link len: ", len(iframe_src_link))


video_links = []
for link in iframe_src_link:
    #print("ifrrame: ", link)
    soup2 = Soup.get(link)
    script_contenent = soup2.find('script', attrs={'type':'text/javascript'})

    in_sting = ""
    for i in script_contenent:
        in_sting += str(i)
    
    # get the begining and the end value to parse the iframe contenent
    begining = "sources: ["
    end = "}],"
    #print("out script link:", ind(begining, end, in_sting))
    script_link_contenent = ind(begining, end, in_sting)

    begining = "{file:"
    end = ",label"
    video_links.append(ind(begining, end, script_link_contenent)[:-1])
    #print(f"video_links: {ind(begining, end, script_link_contenent)[:-1]}\n")
    
f = open(tmp_path,'+a')
ignore_list=[]
for line in open(tmp_path,'r').readlines():
    ignore_list.append(line.strip())

# if one of the movie parsed from url alredy exists in local dawnload path,
# this movie will not be dawnloaded
names =  []
ignored_names =  []
zip_object = zip(titles, video_links)
for title, video_link in zip_object:
    file_name_list = file_list()
    full_title = title + ".mp4"
    if (full_title in file_list()) or (full_title in ignore_list):
        ignored_names.append(title)
        continue
    names.append(title)
    # download_file(video_link, download_link_path, title)
    with open(tmp_path,'a') as file:
        file.write(full_title + '\n')

# to have a log during the each execution from cron
print('Default Link Length: ', len(titles))
if len(names) == 0:
    print("No movie dawnloaded during this execution (Alredy Exists)\n")
else:
    print(f"Number of movie dawnloaded during this execution: {len(names)}\n")
    for i in names:
        print("Downloaded Movie:", i)

for i in ignored_names:
    print("Ignored Movie:", i)



@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hai Nanba  {message.chat.first_name}!**\n\n"
        "**Hey I Am By_Passer Bot Don't Flood A Bot ,Don't Use This Bot Without Getting Permission From Developer**.\n\n **Credits : XCSCXR For His Script**   \n\n **Dev By : @LoveToRide**  ")
@bot.on_message(filters.text & filters.private)
def tex (bot,message):
    check = f'{message.text}'
    rsssc = f'/qbleech {check}'
    
      
  
        
    

    try:
        rss_session.send_message(group_log , rsssc)
    except Exception as e:
         message.reply(f'Error: {e}', quote=True)
        
        
    

@bot.on_message(filters.document & filters.private)
def document (bot,message):
    fileid = f'{message.document.file_id}'
    message.reply(message.caption)
    filecaption = f'{message.caption}'
    
    try:
       
        bot.send_document(message.chat.id , fileid , caption =  filecaption  )
    except Exception as e:
            message.reply(f'Error: {e}', quote=True)
        
    
    #"[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))|magnet:\?xt=urn:btih:[\w!@#$&-?=%.()\\-`.+,/\"]*

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
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**\nTotal Links = {count}**'
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
            txt = f'**🧨ByPassed Url**:</b>**{link_by}****\n\n💣Non_Bypassed Url :{message.text}**\n\n**⭕️Bot_Started By : @{message.chat.username} / {message.chat.id} **\n\n⭕️**Powered By: @TRVPN**\n**\nTotal Links = {count}**'
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

