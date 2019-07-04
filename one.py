import telepot
import os
from pprint import pprint

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telepot.Bot(TOKEN)
print (bot.getMe())