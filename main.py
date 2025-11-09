from handlers.start import start

from telegram.ext import Application, CommandHandler
from config.config import settings
from database.db import Base, engine

TOKEN = settings.TOKEN

Base.metadata.create_all(bind=engine)

def main():
    app = Application.builder().token(TOKEN).build()

    # handlers 


    app.add_handler(CommandHandler("start", start))
    # app.add_handler(ConversationHandler([CommandHandler("register", start_registration)], registration_handler, fallbacks=[CommandHandler("cancel", cancel_registration)]))

    print("Bot is running")
    app.run_polling()

if __name__ == "__main__":
    main()