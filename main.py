# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
import datetime as dt
import telebot
from requests import get
import time
from telebot import types
bot = telebot.TeleBot('1524228050:AAEgIHbTHXik4Ih5InZNh6hCRp0xilj_uvQ')
send = []
print('Код запущен!')

@bot.message_handler(commands=['start'])
def welcome(message):
    print('Бот запущен!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Привет,{}'.format(message.from_user.first_name), parse_mode="html", reply_markup=markup)
    while (1):
        broken = False
        now = dt.datetime.now()
        if now.hour <= 22 and now.hour >= 7:
            print('Бот работает днем')
            p = open('photo.jpg', 'rb')
            bot.send_photo(message.chat.id, p)
        else:
            print('Бот решил поспать :)')
        time.sleep(3600)

bot.polling()