from config.log import setup_logger

logger = setup_logger()

# to get groups id
async def group_id(update,context):
    logger.info(f"Group id is -> {update.message.chat_id}")
