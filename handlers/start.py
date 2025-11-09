from telegram import Update
from telegram.ext import ContextTypes 
from config.log import setup_logger

logger = setup_logger()

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(f"{user.id},{user.first_name},{user.username} -- user has typed start and his data is stored to db")
    await update.message.reply_text("Hello! I'm your simple bot 🤖")
