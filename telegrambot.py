import telebot
from environs import Env
from telebot import types
from random import *
import alhimi


db = alhimi.Database()

env = Env()
env.read_env()
token = env('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if db.get_user(user_id):
        bot.send_message(message.chat.id, "Добро пожаловать!")
    else:
        db.regitser(str(user_id), user_name)
        bot.send_message(message.chat.id, "Спасибо за регистрацию, Добро пожаловать!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    aas1 = types.KeyboardButton("👋 Поздороваться")
    aas2 = types.KeyboardButton("❓ Задать вопрос")
    aas4 = types.KeyboardButton("/shop")
    markup.add(aas1, aas2, aas4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот Масяня".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['shop'])
def start_shop(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("За покупками!", callback_data="startshop"))
    bot.send_message(message.chat.id, f'Меню магазина:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler_shop(call):
    if call.data == "startshop":
        markup = types.InlineKeyboardMarkup()
        shop1 = types.InlineKeyboardButton("🛑Stop🛑", callback_data="finaly_stop")
        shop2 = types.InlineKeyboardButton("Пополнить баланс", callback_data="balanse")
        shop3 = types.InlineKeyboardButton("Зайти в магазин", callback_data="magazin")
        markup.add(shop2, shop1, shop3)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "balanse":
        markup = types.InlineKeyboardMarkup()
        sh1 = types.InlineKeyboardButton("Назад", callback_data="nazad")
        sh2 = types.InlineKeyboardButton("+1000", callback_data="1000")
        sh3 = types.InlineKeyboardButton("+2000", callback_data="2000")
        sh4 = types.InlineKeyboardButton("+3000", callback_data="3000")
        sh5 = types.InlineKeyboardButton("+4000", callback_data="4000")
        sh6 = types.InlineKeyboardButton("+5000", callback_data="5000")
        markup.add(sh2, sh1, sh6, sh3, sh4, sh5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "1000":
        user_id = call.from_user.id
        db.update_balance(user_id, "1000", True)
        bot.send_message(call.message.chat.id, text=f"Ваш баланс пополнился на 1000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "2000":
        user_id = call.from_user.id
        db.update_balance(user_id, "2000", True)
        bot.send_message(call.message.chat.id, text=f"Ваш баланс пополнился на 2000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "3000":
        user_id = call.from_user.id
        db.update_balance(user_id, "3000", True)
        bot.send_message(call.message.chat.id, text=f"Ваш баланс пополнился на 3000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "4000":
        user_id = call.from_user.id
        db.update_balance(user_id, "4000", True)
        bot.send_message(call.message.chat.id, text=f"Ваш баланс пополнился на 4000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "5000":
        user_id = call.from_user.id
        db.update_balance(user_id, "5000", True)
        bot.send_message(call.message.chat.id, text=f"Ваш баланс пополнился на 5000. Ваш баланс: {db.get_balance(user_id)}" )

    elif call.data == "magazin":
        markup = types.InlineKeyboardMarkup()
        sh1 = types.InlineKeyboardButton("⇧Назад⇧", callback_data="nazad")
        magazin1 = types.InlineKeyboardButton("Напитки🥃", callback_data="beverages")
        magazin2 = types.InlineKeyboardButton("Хлебобулки🍞", callback_data="bakery")
        magazin3 = types.InlineKeyboardButton("Кондитерка🍣", callback_data="confectioner")
        magazin4 = types.InlineKeyboardButton("Химия🧪", callback_data="chemistry")
        magazin5 = types.InlineKeyboardButton("Молочка🥛", callback_data="milk")
        markup.add(magazin1, sh1, magazin2, magazin3, magazin4, magazin5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "bakery":
        markup = types.InlineKeyboardMarkup()
        sh11 = types.InlineKeyboardButton("⇧Вернуться⇧", callback_data="nazad1")
        bakery1 = types.InlineKeyboardButton("Белый хлеб🍞 - 1000", callback_data="white_bread")
        bakery2 = types.InlineKeyboardButton("Чёрный хлеб🍞 - 900", callback_data="black_bread")
        bakery3 = types.InlineKeyboardButton("Плюшка🥨 - 800", callback_data="bun")
        bakery4 = types.InlineKeyboardButton("Вафля🧇 - 900", callback_data="cheesecake")
        bakery5 = types.InlineKeyboardButton("Лаваш - 500", callback_data="pita")
        bakery6 = types.InlineKeyboardButton("Бублик🥯 - 300", callback_data="bagel")
        bakery7 = types.InlineKeyboardButton("Баранки🥯🥯 - 1300", callback_data="bagels")
        markup.add(bakery1, sh11, bakery2, bakery3, bakery4, bakery5, bakery6, bakery7)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "white_bread":
        user_id = call.from_user.id
        db.update_balance(user_id, "1000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили белый хлеб🍞.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "black_bread":
        user_id = call.from_user.id
        db.update_balance(user_id, "900", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили чёрный хлеб🍞.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 900. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "bun":
        user_id = call.from_user.id
        db.update_balance(user_id, "800", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили плюшку🥨.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 800. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "cheesecake":
        user_id = call.from_user.id
        db.update_balance(user_id, "900", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили вафлю🧇.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 900. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "pita":
        user_id = call.from_user.id
        db.update_balance(user_id, "500", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили лаваш.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 500. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "bagel":
        user_id = call.from_user.id
        db.update_balance(user_id, "300", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили бублик🥯.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 300. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "bagels":
        user_id = call.from_user.id
        db.update_balance(user_id, "1300", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили баранки🥯🥯.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1300. Ваш баланс: {db.get_balance(user_id)}" )


    elif call.data == "beverages":
        markup = types.InlineKeyboardMarkup()
        sh11 = types.InlineKeyboardButton("⇧Вернуться⇧", callback_data="nazad1")
        beverages1 = types.InlineKeyboardButton("Вода🧊 - 300", callback_data="water")
        beverages2 = types.InlineKeyboardButton("Лимонад🥤 - 400", callback_data="lemon")
        beverages3 = types.InlineKeyboardButton("Сок🧃 - 500", callback_data="juice")
        beverages4 = types.InlineKeyboardButton("Энергетик - 800", callback_data="energy_drink")
        beverages5 = types.InlineKeyboardButton("Чай - 600", callback_data="tea")
        beverages6 = types.InlineKeyboardButton("Шампанское🍾 - 3000", callback_data="champagne")
        beverages7 = types.InlineKeyboardButton("Вино🍷 - 6000", callback_data="wine")
        markup.add(beverages1, sh11, beverages2, beverages3, beverages4, beverages5, beverages6, beverages7)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "water":
        user_id = call.from_user.id
        db.update_balance(user_id, "300", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили воду🧊.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 300. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "lemon":
        user_id = call.from_user.id
        db.update_balance(user_id, "400", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили лимонад🥤.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 400. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "juice":
        user_id = call.from_user.id
        db.update_balance(user_id, "500", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили сок🧃.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 500. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "energy_drink":
        user_id = call.from_user.id
        db.update_balance(user_id, "800", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили энергетик🍸.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 800. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "tea":
        user_id = call.from_user.id
        db.update_balance(user_id, "600", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили чай☕.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 600. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "champagne":
        user_id = call.from_user.id
        db.update_balance(user_id, "3000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили шампанское🍾.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 3000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "wine":
        user_id = call.from_user.id
        db.update_balance(user_id, "6000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили вино🍷.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 6000. Ваш баланс: {db.get_balance(user_id)}" )


    elif call.data == "confectioner":
        markup = types.InlineKeyboardMarkup()
        sh11 = types.InlineKeyboardButton("⇧Вернуться⇧", callback_data="nazad1")
        confectioner1 = types.InlineKeyboardButton("Конфеты🍬🍬 - 2000", callback_data="candies")
        confectioner2 = types.InlineKeyboardButton("Зефир🧁 - 3000", callback_data="marshmallows")
        confectioner3 = types.InlineKeyboardButton("Пастила🍮 - 2800", callback_data="paste")
        confectioner4 = types.InlineKeyboardButton("Печенье🍪 - 2400", callback_data="cookie")
        confectioner5 = types.InlineKeyboardButton("Круасанны🥐 - 3400", callback_data="croissants")
        confectioner6 = types.InlineKeyboardButton("Шоколадка🍫 - 2300", callback_data="chocolate")
        markup.add(confectioner1, sh11, confectioner2, confectioner3, confectioner4, confectioner5, confectioner6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "candies":
        user_id = call.from_user.id
        db.update_balance(user_id, "2000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили конфеты🍬🍬.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 2000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "marshmallows":
        user_id = call.from_user.id
        db.update_balance(user_id, "3000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили зефир🧁.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 3000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "paste":
        user_id = call.from_user.id
        db.update_balance(user_id, "2800", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили пастилу🍮.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 2800. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "cookie":
        user_id = call.from_user.id
        db.update_balance(user_id, "2400", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили печенье🍪.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 2400. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "croissants":
        user_id = call.from_user.id
        db.update_balance(user_id, "3400", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили круассаны🥐.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 3400. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "chocolate":
        user_id = call.from_user.id
        db.update_balance(user_id, "2300", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили шоколадку🍫.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 2300. Ваш баланс: {db.get_balance(user_id)}" )

    
    elif call.data == "chemistry":
        markup = types.InlineKeyboardMarkup()
        sh11 = types.InlineKeyboardButton("⇧Вернуться⇧", callback_data="nazad1")
        chemistry1 = types.InlineKeyboardButton("Мыло🧼 - 1200", callback_data="soap")
        chemistry2 = types.InlineKeyboardButton("Стиральный порошок - 12000", callback_data="washing_powder")
        chemistry3 = types.InlineKeyboardButton("Освежитель воздуха🦨 - 7800", callback_data="bleach")
        chemistry4 = types.InlineKeyboardButton("Отбеливатель - 5500", callback_data="air_freshener")
        markup.add(chemistry1, sh11, chemistry2, chemistry3, chemistry4)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "soap":
        user_id = call.from_user.id
        db.update_balance(user_id, "1200", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили мыло🧼.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1200. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "washing_powder":
        user_id = call.from_user.id
        db.update_balance(user_id, "12000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили стиральный порошок.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 12000. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "bleach":
        user_id = call.from_user.id
        db.update_balance(user_id, "7800", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили освежитель воздуха🦨.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 7800. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "air_freshener":
        user_id = call.from_user.id
        db.update_balance(user_id, "5500", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили отбеливатель.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 5500. Ваш баланс: {db.get_balance(user_id)}" )


    elif call.data == "milk":
        markup = types.InlineKeyboardMarkup()
        sh11 = types.InlineKeyboardButton("⇧Вернуться⇧", callback_data="nazad1")
        milk1 = types.InlineKeyboardButton("Молоко🥛 - 1200", callback_data="milks")
        milk2 = types.InlineKeyboardButton("Сыр🧀 - 2400", callback_data="cheese")
        milk3 = types.InlineKeyboardButton("Творог - 1900", callback_data="cottage_cheese")
        milk4 = types.InlineKeyboardButton("Йогурт🍶 - 1300", callback_data="yogurt")
        milk5 = types.InlineKeyboardButton("Сырок - 1000", callback_data="cheeses")
        markup.add(milk1, sh11, milk2, milk3, milk4, milk5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "milks":
        user_id = call.from_user.id
        db.update_balance(user_id, "1200", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили молоко🥛.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1200. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "cheese":
        user_id = call.from_user.id
        db.update_balance(user_id, "2400", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили сыр🧀.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 2400. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "cottage_cheese":
        user_id = call.from_user.id
        db.update_balance(user_id, "1900", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили творог.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1900. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "yogurt":
        user_id = call.from_user.id
        db.update_balance(user_id, "1300", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили йогурт🍶.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1300. Ваш баланс: {db.get_balance(user_id)}" )
    elif call.data == "cheeses":
        user_id = call.from_user.id
        db.update_balance(user_id, "1000", False)
        bot.send_message(call.message.chat.id, text="Поздравляю! Вы купили сырок.")
        bot.send_message(call.message.chat.id, text=f"Ваш баланс понизился на 1000. Ваш баланс: {db.get_balance(user_id)}" )


    elif call.data == "nazad1":
        markup = types.InlineKeyboardMarkup()
        sh1 = types.InlineKeyboardButton("⇧Назад⇧", callback_data="nazad")
        magazin1 = types.InlineKeyboardButton("Напитки🥃", callback_data="beverages")
        magazin2 = types.InlineKeyboardButton("Хлебобулки🍞", callback_data="bakery")
        magazin3 = types.InlineKeyboardButton("Кондитерка🍣", callback_data="confectioner")
        magazin4 = types.InlineKeyboardButton("Химия🧪", callback_data="chemistry")
        magazin5 = types.InlineKeyboardButton("Молочка🥛", callback_data="milk")
        markup.add(magazin1, sh1, magazin2, magazin3, magazin4, magazin5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "nazad":
        markup = types.InlineKeyboardMarkup()
        shop1 = types.InlineKeyboardButton("🛑Stop🛑", callback_data="finaly_stop")
        shop2 = types.InlineKeyboardButton("Пополнить баланс", callback_data="balanse")
        shop3 = types.InlineKeyboardButton("Зайти в магазин", callback_data="magazin")
        markup.add(shop2, shop1, shop3)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "finaly_stop":
        bot.delete_message(call.message.chat.id, call.message.message_id)
    

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет..)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        aas1 = types.KeyboardButton("Как меня зовут?")
        aas2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(aas1, aas2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "Меня зовут Масяня.")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        aas1 = types.KeyboardButton("👋 Поздороваться")
        aas2 = types.KeyboardButton("❓ Задать вопрос")
        aas4 = types.KeyboardButton("/shop")
        markup.add(aas1, aas2, aas4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

bot.polling(none_stop=True)
