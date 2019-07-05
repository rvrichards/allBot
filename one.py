import telepot
import os
from telepot.loop import MessageLoop
from pprint import pprint

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telepot.Bot(TOKEN)
print (bot.getMe())



def handle(msg):
	print (msg)

MessageLoop(bot, handle).run_as_thread()	