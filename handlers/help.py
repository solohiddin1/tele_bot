from telegram import Update
from telegram.ext import ContextTypes 
from database.db import SessionLocal
from config.log import setup_logger

logger = setup_logger()


# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(f"{user.id},{user.first_name},{user.username} -- user is trying to get help")
    await update.message.reply_text("I only know /start , /help and /admin xabar  for now.")
