from telegram import Bot
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv('SECRET_KEY')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send_telegram_message(message):
    bot_token = TELEGRAM_TOKEN
    chat_id = TELEGRAM_CHAT_ID
    
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    



