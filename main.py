import os
import telegram

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")
  
updater = Updater(token=TOKEN)
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()


#bot = telegram.Bot(TOKEN)
#bot.send_messge(update.message.chat_id, '123')
