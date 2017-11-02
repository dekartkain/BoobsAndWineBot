import os
import telegram

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']

bot = telegram.Bot(TOKEN)

bot.send_messge(update.message.chat_id, '123')
