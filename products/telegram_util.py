from telegram import Bot

async def send_telegram_message(message):
    bot_token = '5045449249:AAFB1tNU_X8xOQI-rGCWyLhi2JU-RwRrcfU'
    chat_id = '1234416899'
    
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    



