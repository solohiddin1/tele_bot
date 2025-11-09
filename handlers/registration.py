from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, filters, MessageHandler
from database.db import SessionLocal
from database.user import User
from config.log import setup_logger

logger = setup_logger()

# Conversation states
NAME, PHONE, LOGIN = range(3)


async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the registration process"""
    await update.message.reply_text(
        "Ro'yxatdan o'tish jarayoni boshlandi.\n\n"
        "Iltimos, ismingizni kiriting:"
    )
    return NAME


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get user's name"""
    name = update.message.text.strip()
    if not name or len(name) < 2:
        await update.message.reply_text(
            "Iltimos, to'g'ri ism kiriting (kamida 2 ta belgi):"
        )
        return NAME
    
    context.user_data['name'] = name
    await update.message.reply_text(
        f"Yaxshi, {name}!\n\n"
        "Endi telefon raqamingizni kiriting (masalan: +998901234567 yoki 901234567):"
    )
    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get user's phone number"""
    phone = update.message.text.strip()
    
    # Basic phone validation (remove spaces and check if it's numeric or has +)
    phone_clean = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    if not phone_clean or (not phone_clean.startswith("+") and not phone_clean.isdigit()):
        await update.message.reply_text(
            "Iltimos, to'g'ri telefon raqam kiriting (masalan: +998901234567 yoki 901234567):"
        )
        return PHONE
    
    context.user_data['phone_number'] = phone_clean
    await update.message.reply_text(
        "Telefon raqam qabul qilindi!\n\n"
        "Endi login kiriting:"
    )
    return LOGIN


async def get_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get user's login and complete registration"""
    login = update.message.text.strip()
    
    if not login or len(login) < 3:
        await update.message.reply_text(
            "Iltimos, login kiriting (kamida 3 ta belgi):"
        )
        return LOGIN
    
    # Check if login already exists
    db = SessionLocal()
    existing_user = db.query(User).filter(User.login == login).first()
    
    if existing_user:
        db.close()
        await update.message.reply_text(
            "Bu login allaqachon ishlatilgan. Iltimos, boshqa login kiriting:"
        )
        return LOGIN
    
    # Get user data from context
    user_id = update.message.from_user.id
    name = context.user_data.get('name')
    phone_number = context.user_data.get('phone_number')
    username = update.message.from_user.username
    
    # Save or update user in database
    user = db.get(User, user_id)
    if user:
        # Update existing user
        user.name = name
        user.phone_number = phone_number
        user.login = login
        user.username = username
    else:
        # Create new user
        user = User(
            id=user_id,
            name=name,
            username=username,
            phone_number=phone_number,
            login=login
        )
        db.add(user)
    
    db.commit()
    db.close()
    
    # Clear user data
    context.user_data.clear()
    
    logger.info(f"User {user_id} ({name}) registered with login: {login}, phone: {phone_number}")
    
    await update.message.reply_text(
        f"🎉 Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n\n"
        f"📝 Ism: {name}\n"
        f"📱 Telefon: {phone_number}\n"
        f"🔑 Login: {login}\n\n"
        f"Ma'lumotlaringiz saqlandi!"
    )
    
    return ConversationHandler.END


async def cancel_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel the registration process"""
    context.user_data.clear()
    await update.message.reply_text("Ro'yxatdan o'tish bekor qilindi.")
    return ConversationHandler.END


# Create the conversation handler
registration_handler = ConversationHandler(
    entry_points=[CommandHandler("register", start_registration)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        LOGIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_login)],
    },
    fallbacks=[CommandHandler("cancel", cancel_registration)],
)

