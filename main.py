import os
import telegram

TOKEN = os.environ['PP_BOT_TOKEN']
URL = os.environ['PP_BOT_URL']
REPO = os.environ['PP_BOT_REPO']

bot = telegram.Bot(TOKEN)


if __name__ == '__main__':
    main()
