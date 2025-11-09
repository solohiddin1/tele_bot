from telegram import Update, Bot
from telegram.ext import ContextTypes 
from database.db import SessionLocal
from database.user import User
from config.log import setup_logger
from get_music import music

from helpers.download_audio import download_video, check_file_size

import os
import re
import html

logger = setup_logger()


def sanitize(title):
    return re.sub(r'[\\/*?:"<>|｜%]', "", title)


# link to you tube
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        link = update.message.text
        logger.info(link)
        mus = await music(link)
        logger.info(f"this is mus ------> {mus}")
        
        print(mus)
        # first = mus["items"][0]["snippet"]
        # title = first["title"]
        url = f"https://www.youtube.com/watch?v={mus['items'][0]['id']['videoId']}"
        title = html.unescape(mus["items"][0]["snippet"]["title"])
        print("-------------",title)
        clean_title = sanitize(title)
        print("-------------",clean_title)

        file_name = f"audios/{clean_title}.mp3"
        logger.info(f"Filename - {file_name}")
        if os.path.exists(file_name):
            audio = file_name
            print("entered to root============")
            await update.message.reply_audio(open(audio,"rb"))
        else:
            if check_file_size(url):
                audio = download_video(url)
                await update.message.reply_audio(open(audio,"rb"))
            else:
                await update.message.reply_text(f"File is too large to download;")
    except Exception as e:
        logger.info(f"not found!  - {e}")
        await update.message.reply_text(f"sorry nothing found!")

# link("this")
# # group id
# async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     link = update.message.chat.id
#     logger.info(link)
#     await Bot.send_message(chat_id=8023512848,text="dasd")
