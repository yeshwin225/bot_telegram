!pip install adafruit-io
import os
x = "yeshwin_hero" #ADAFRUIT_IO_USERNAME
y = "aaio_OmZg66j2EVFW8hLkyQqwWL3DENnt"  #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(x,y)
# Create a feed
new = Feed(name='yeshwinbot')  # Feed name is given
result = aio.create_feed(new)
!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth turned on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=1)
    value_send = aio.create_data('yeshwinbot',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth turned off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=0)
    value_send = aio.create_data('yeshwinbot',value)


u = Updater('1375651391:AAFknAHfkfMko4J2SDIrgyBC5aVw077phE')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
