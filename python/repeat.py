import os
import sys
import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

#
# repeat.py - mostly repeat anything heard at goflyakite_bot
#
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print (content_type, chat_type, chat_id)
    command = msg.get('text', 'empty')  # If there is no 'text' command, assign 'empty'
    print ("Command", command)

    if command  == '/hello':
        bot.sendMessage(chat_id, "Is it me you're looking for?")
    elif command  == '/goodbye':
        bot.sendPhoto(chat_id, 'http://rtfm.ca/data/YellowBrickRoad.jpg')
    elif content_type == 'document':
        bot.sendMessage(chat_id, "I'll check that out later.")
    elif content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
    elif content_type == 'sticker':
        bot.sendMessage(chat_id, "I'm stuck with this. :(")
    elif content_type == 'photo':
    	if msg['caption'] is not None:
    		bot.sendMessage(chat_id, 'Back at you.')
    	bot.sendPhoto(chat_id, 'https://source.unsplash.com/444x666/?water,ocean,mountain')
    else:
    	bot.sendMessage(chat_id, 'I am not sure.')

TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Lets roll ...')

# Do forever undtil cntl+c
while 1:
    time.sleep(6.66)