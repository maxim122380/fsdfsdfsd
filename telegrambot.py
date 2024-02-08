import telebot
from environs import Env
from telebot import types
from random import *


env = Env()
env.read_env()
token = env('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🟩Начать", callback_data="start"))
    bot.send_message(message.chat.id, f'Меню программы:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "start":
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton("Маркетплейсы", callback_data="market")
        btn3 = types.InlineKeyboardButton("Заказать еду", callback_data="eating")
        btn4 = types.InlineKeyboardButton("Техно-блог", callback_data="tecno")
        btn5 = types.InlineKeyboardButton("Техника", callback_data="texnika")
        btn6 = types.InlineKeyboardButton("Писатели", callback_data="pisary")
        markup.add(btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "pisary":
        markup = types.InlineKeyboardMarkup()
        p1 = types.InlineKeyboardButton("🟥Вернуться🟥", callback_data="stop")
        p2 = types.InlineKeyboardButton("Пушкин", callback_data="pushkin", url="https://www.culture.ru/persons/8195/aleksandr-pushkin")
        p3 = types.InlineKeyboardButton("Лермонтов", callback_data="lermontov", url="https://www.culture.ru/persons/8188/mikhail-lermontov")
        p4= types.InlineKeyboardButton("Толстой", callback_data="tolstoy", url="https://www.culture.ru/persons/8211/lev-tolstoi")
        p5 = types.InlineKeyboardButton("Гоголь", callback_data="gogol", url="https://www.culture.ru/persons/8127/nikolai-gogol")
        p6 = types.InlineKeyboardButton("Достоевский", callback_data="dostoevskty", url="https://www.culture.ru/persons/8159/fedor-dostoevskii")
        p7 = types.InlineKeyboardButton("Чехов", callback_data="chexov", url="https://www.culture.ru/persons/8209/anton-chekhov")
        p8 = types.InlineKeyboardButton("Есенин", callback_data="esenin", url="https://www.culture.ru/persons/8133/sergei-esenin")
        p9 = types.InlineKeyboardButton("Грибоедов", callback_data="griboedov", url="https://www.culture.ru/persons/8210/aleksandr-griboedov")
        markup.add(p5, p2, p3, p4, p1, p6, p7, p8, p9)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "market":
        markup = types.InlineKeyboardMarkup()
        bt1 = types.InlineKeyboardButton("🟥Вернуться🟥", callback_data="stop")
        bt2 = types.InlineKeyboardButton("Ozon", callback_data="ozon", url="https://www.ozon.ru/")
        bt3 = types.InlineKeyboardButton("Wildberries", callback_data="wildberries", url="https://www.wildberries.ru/")
        bt4= types.InlineKeyboardButton("Aliexpress", callback_data="aliexpress", url="https://aliexpress.ru/")
        bt5 = types.InlineKeyboardButton("Яндекс.Маркет", callback_data="YandexMarket", url="https://market.yandex.ru/")
        markup.add(bt2, bt1, bt3, bt4, bt5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    
    elif call.data == "tecno":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🟥Вернуться🟥", callback_data="stop")
        b2 = types.InlineKeyboardButton("Wylsacom", callback_data="wylsacom", url="https://t.me/Wylsared")
        b3 = types.InlineKeyboardButton("Romancev768", callback_data="romancev768", url="https://t.me/Romancev768")
        b4 = types.InlineKeyboardButton("Наука и техника", callback_data="science", url="https://t.me/Scienceg")
        b5 = types.InlineKeyboardButton("Apple News", callback_data="applenews", url="https://t.me/apple_tg")
        markup.add(b2, b1, b3, b4, b5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)


    elif call.data == "eating":
        markup = types.InlineKeyboardMarkup()
        btt1 = types.InlineKeyboardButton("🟥Вернуться🟥", callback_data="stop")
        btt2 = types.InlineKeyboardButton("Додо Пицца", callback_data="dodopizza", url="https://dodopizza.ru/")
        btt3 = types.InlineKeyboardButton("ТоТо Пицца", callback_data="totopizza", url="https://kovrov.totopizza.ru/")
        btt4= types.InlineKeyboardButton("Бургер Кинг", callback_data="burgerking", url="https://burgerkingrus.ru/")
        btt5 = types.InlineKeyboardButton("Вкусно и Точка", callback_data="vkusnoitochka", url="https://vkusnoitochka.ru/")
        btt6 = types.InlineKeyboardButton("Ростикс", callback_data="kfc", url="https://rostics.ru/")
        markup.add(btt2, btt1, btt3, btt4, btt5, btt6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "texnika":
        markup = types.InlineKeyboardMarkup()
        s1 = types.InlineKeyboardButton("🟥Вернуться🟥", callback_data="stop")
        s2 = types.InlineKeyboardButton("DNS", callback_data="dns", url="https://www.dns-shop.ru/")
        s3 = types.InlineKeyboardButton("М.видео", callback_data="mvideo", url="https://www.mvideo.ru/")
        s4= types.InlineKeyboardButton("Эльдорадо", callback_data="eldorado", url="https://www.eldorado.ru/?utm_source=google&utm_medium=organic&utm_campaign=google&utm_referrer=google")
        s5 = types.InlineKeyboardButton("Ситилинк", callback_data="citilink", url="https://www.citilink.ru/")
        s6 = types.InlineKeyboardButton("Онлайн Трейд", callback_data="onlinetreid", url="https://www.onlinetrade.ru/?utm_referrer=https%3a%2f%2fwww.google.com%2f")
        markup.add(s2, s1, s3, s4, s5, s6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "stop":
        markup = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton("Маркетплейсы", callback_data="market")
        btn3 = types.InlineKeyboardButton("Заказать еду", callback_data="eating")
        btn4 = types.InlineKeyboardButton("Техно-блог", callback_data="tecno")
        btn5 = types.InlineKeyboardButton("Техника", callback_data="texnika")
        btn6 = types.InlineKeyboardButton("Писатели", callback_data="pisary")
        markup.add(btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

bot.polling(none_stop=True)
