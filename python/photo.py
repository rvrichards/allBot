import os
import time
import telepot
from telepot.loop import MessageLoop
import cv2 as cv
import tempfile


# This will grab a photo, load it to temp file, convert it and send it back.

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	# print (content_type, chat_type, chat_id)
	if content_type == 'photo' :
		chat_id = msg['chat']['id']
		f=tempfile.NamedTemporaryFile(delete=True).name+".png"
		photo  = msg['photo'][-1]["file_id"]
		path = bot.getFile(photo)["file_path"]
		bot.sendMessage(chat_id, "Converting to grayscale file: %s" % path)
		bot.download_file(photo,f)
		p = cv.imread(f)
		cv.imwrite(f, cv.cvtColor(p, cv.COLOR_BGR2GRAY))
		bot.sendPhoto(chat_id, open(f, 'rb'))
	else:
		bot.sendMessage(chat_id, "I'm thankful for this. :)")

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Lets roll ...')

# Do forever until cntl+c
while 1:
    time.sleep(6.66)