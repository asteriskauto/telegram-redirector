#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import telebot
import sys

token = '353egervsdv6DVdVS7dv6sDVSvsd7v6s57vsdvs6d7v5' # Вводим свой телеграм API токен
group_id = -123456789 # Вводим id группы, куда надо слать сообщения (int с отрицательным значением)
bot = telebot.TeleBot(token, skip_pending=True)

# Ловим команду старта при старте без аргументов (первый старт)
@bot.message_handler(func=lambda message: True, commands=['start'])
def start(message):
    if len(sys.argv) != 1:
        return
    bot.send_message(message.chat.id, "ID чата: " + str(message.chat.id))
    print message.chat.id
    sys.exit()

# Если был передан один аргумент, то возвращаем в чат сообщение
if len(sys.argv) == 2:
    number = str(sys.argv[1])
    bot.send_message(group_id, "Вызова с номера " + number)

# Если аргумента нет, то считаем первым стартом и запускаем в режиме полинга
if len(sys.argv) == 1:
    bot.polling(none_stop=True)
