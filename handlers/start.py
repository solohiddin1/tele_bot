from telegram import Update
from telegram.ext import ContextTypes 
from database.db import SessionLocal
from database.user import User
from config.log import setup_logger


logger = setup_logger()


# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SessionLocal()
    user = update.message.from_user
    if not db.get(User,user.id):
        db.add(User(id=user.id,name=user.first_name,username=user.username,))
        db.commit()
    db.close()
    # print(user.id,user.first_name,user.username)
    logger.info(f"{user.id},{user.first_name},{user.username} -- user has typed start and his data is stored to db")
    await update.message.reply_text("Hello! I'm your simple bot 🤖")
