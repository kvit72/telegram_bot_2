"""Telegram бот отвечающий пользователю на его текстовые сообщения и стикеры."""

import telebot
from telebot import types

bot = telebot.TeleBot('')
# Указываем токен для бота.

@bot.message_handler(commands=['start'])
# Отслеживаем команду старт.
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>."
    # Текст приветствия.

    sti = open('jsins.webp', 'rb')
    # Стикер приветствия.
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
# Отслеживаем текст отправленный пользователем.
def get_user_text(message):
    if message.text == "hello":
        # Отвечаем пользователю текстовым сообщением.
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == "id":
        # Отображаем пользователю его telegram id.
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        # Отвечаем пользователю картинкой.
        photo = open('car.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "website":
        # Отвечаем пользователю сообщением и кнопкой перехода на веб сайт.
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://dzen.ru/"))
        bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)
    elif message.text == "help":
        # Выводим две кнопки меню под строкой ввода сообщения.
        markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        website = types.KeyboardButton('Веб сайт')
        start = types.KeyboardButton('Start')
        markup_2.add(website, start)
        bot.send_message(message.chat.id, reply_markup=markup_2)
    else:
        # Отвечаем пользователю, в случае ввода им текста отличного от вышеуказанного.
        bot.send_message(message.chat.id, "Я тебя не понимаю.", parse_mode='html')


@bot.message_handler(content_types=['sticker'])
# Отслеживаем стикеры отправленные пользователем.
def get_user_sticker(message):
    bot.send_message(message.chat.id, "Прикольный стикер!", parse_mode='html')


bot.polling(none_stop=True)
# Данным методом бот запускается на постоянную обработку.