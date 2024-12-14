import telebot
from telebot import types
TOKEN = '7402197318:AAEUceMHPwz8CHtL38briaiI6RTyCGhHMYA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("القائمة")  
    markup.add(button)
    bot.send_message(message.chat.id, "مرحبا بك في بوت المواد الدراسية", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "القائمة")
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("رياضة")
    button2 = types.KeyboardButton("لا شيء")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,"قم باختيار المادة التي تريدها", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "رياضة")
def math(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    u1 = types.KeyboardButton("الوحدة الاولة")
    u2 = types.KeyboardButton("الوحدة الثانية")
    keyboard.add(u2, u1)
    bot.send_message(message.chat.id,"hi", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "الوحدة الاولة")
def u1(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    l1 = types.KeyboardButton("الدرس الاول")
    l2 = types.KeyboardButton("الدرس الثاني")
    l3 = types.KeyboardButton("الدرس الثالث")
    l4 = types.KeyboardButton("الدرس الرابع")
    l5 = types.KeyboardButton("الدرس الخامس")
    l6 = types.KeyboardButton("الدرس السادس")
    l7 = types.KeyboardButton("الدرس السابع")
    l8 = types.KeyboardButton("الدرس الثامن")
    l9 = types.KeyboardButton("الدرس التاسع")
    l10 = types.KeyboardButton("الدرس العاشر")
    keyboard.add(l3, l2, l1, l6, l5, l4, l9, l8, l7, l10)
    bot.send_message(message.chat.id,"قم بأختيار الدرس الذي تريد معرفة شرحه", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "الدرس الاول")
def l1(message):
    inline = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("مثال 1",callback_data="m1")
    button2 = types.InlineKeyboardButton("مثال 2",callback_data="m2")
    button3 = types.InlineKeyboardButton("مثال 3",callback_data="m3")
    button4 = types.InlineKeyboardButton("مثال 4",callback_data="m4")
    button5 = types.InlineKeyboardButton("مثال 5",callback_data="m5")
    button6 = types.InlineKeyboardButton("مثال 6",callback_data="m6")
    button7 = types.InlineKeyboardButton("مثال 7",callback_data="m7")
    inline.add(button1, button2, button3, button4, button5, button6, button7)
    bot.send_message(message.chat.id, """الدرس الاول : القوى الصحيحة غير السالبة""")

    photo = open("math/math u1.1.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)    


@bot.message_handler(func=lambda message: message.text == "الدرس الثاني")
def l2(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال  1",callback_data="1.2.1")
    m2 = types.InlineKeyboardButton("مثال  2",callback_data="1.2.2")
    inline.add(m1, m2)
    bot.send_message(message.chat.id, """الدرس الثاني : القوى الصحيحة السالبة""")
    photo = open("math/math u1.2.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)

@bot.message_handler(func=lambda message: message.text == "الدرس الثالث")
def l3(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.3.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.3.2")
    m3 = types.InlineKeyboardButton("مثال 3",callback_data="1.3.3")
    m4 = types.InlineKeyboardButton("مثال 4",callback_data="1.3.4")
    inline.add(m1, m2, m3, m4)
    bot.send_message(message.chat.id, """الدرس الثالث : القوة الكسرية""")
    photo = open("math/math u1.3.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)


@bot.message_handler(func=lambda message: message.text == "الدرس الرابع")
def l4(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.4.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.4.2")
    m3 = types.InlineKeyboardButton("مثال 3",callback_data="1.4.3")
    m4 = types.InlineKeyboardButton("مثال 4",callback_data="1.4.4")
    m5 = types.InlineKeyboardButton("مثال 5",callback_data="1.4.5")
    m6 = types.InlineKeyboardButton("مثال 6",callback_data="1.4.6")
    inline.add(m1, m2, m3, m4, m5, m6)
    bot.send_message(message.chat.id, """الدرس الرابع : حل المعادلات الاسية""")
    photo = open("math/math u1.4.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)

@bot.message_handler(func=lambda message: message.text == "الدرس الخامس")
def l5(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.5.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.5.2")
    m3 = types.InlineKeyboardButton("مثال 3",callback_data="1.5.3")
    inline.add(m1, m2, m3)
    bot.send_message(message.chat.id, """الدرس الخامس : تطبيقات على المعادلات الاسية""")
    photo = open("math/math u1.5.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)


@bot.message_handler(func=lambda message: message.text == "الدرس السادس")
def l6(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.6.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.6.2")
    m3 = types.InlineKeyboardButton("مثال 3",callback_data="1.6.3")
    m4 = types.InlineKeyboardButton("مثال 4",callback_data="1.6.4")
    inline.add(m1, m2, m3, m4)
    bot.send_message(message.chat.id, """الدرس السادس : الدالة اللوغارتمية""")
    photo = open("math/math u1.6.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)


@bot.message_handler(func=lambda message: message.text == "الدرس السابع")
def l7(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.7.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.7.2")
    m3 = types.InlineKeyboardButton("مثال 3",callback_data="1.7.3")
    m4 = types.InlineKeyboardButton("مثال 4",callback_data="1.7.4")
    inline.add(m1, m2, m3, m4)
    bot.send_message(message.chat.id, """الدرس السابع : خواص الدالة اللوغارتمية""")
    photo = open("math/math u1.7.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)


@bot.message_handler(func=lambda message: message.text == "الدرس الثامن")
def l8(message):
    inline = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton("مثال 1",callback_data="1.8.1")
    m2 = types.InlineKeyboardButton("مثال 2",callback_data="1.8.2")
    inline.add(m1, m2)
    bot.send_message(message.chat.id, """الدرس الثامن : تابع خواص الدالة اللوغارتمية""")
    photo = open("math/math u1.8.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)


@bot.message_handler(func=lambda message: message.text == "الدرس التاسع")
def l9(message):
    bot.send_message(message.chat.id,"الدرس التاسع : استخدام الالة الحاسبة في الدوال اللوغارتمية")
    photo = open("math/math u1.9.png", "rb")
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda message: message.text == "الدرس العاشر")
def l10(message):
    inline = types.InlineKeyboardMarkup()
    m1  = types.InlineKeyboardButton("مثال 1",callback_data="1.10.1")
    m2  = types.InlineKeyboardButton("مثال 2",callback_data="1.10.2")
    inline.add(m1, m2)
    bot.send_message(message.chat.id,"الدرس العاشر : حل المعادلات الاسية")
    photo = open("math/math u1.10.png", "rb")
    bot.send_photo(message.chat.id, photo, reply_markup=inline)
@bot.callback_query_handler(func=lambda call:True)
def callback_l(call):
        if call.data == "m1":
            photo = open("math/math1.1.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "m2":
            photo = open("math/math1.1.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "m3":
            photo = open("math/math1.1.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "m4":
            photo = open("math/math1.1.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "m5":
            photo = open("math/math1.1.5.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 5")
        elif call.data == "m6":
            photo = open("math/math1.1.6.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 6")
        elif call.data == "m7":
            photo = open("math/math1.1.7.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 7")
        elif call.data == "1.2.1":
            photo = open("math/math1.2.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.2.2":
            photo = open("math/math1.2.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.3.1":
            photo = open("math/math1.3.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.3.2":
            photo = open("math/math1.3.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.3.3":
            photo = open("math/math1.3.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.3.4":
            photo = open("math/math1.3.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "1.4.1":
            photo = open("math/math1.4.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.4.2":
            photo = open("math/math1.4.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.4.3":
            photo = open("math/math1.4.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.4.4":
            photo = open("math/math1.4.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "1.4.5":
            photo = open("math/math1.4.5.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 5")
        elif call.data == "1.4.6":
            photo = open("math/math1.4.6.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 6")
        elif call.data == "1.5.1":
            photo = open("math/math1.5.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.5.2":
            photo = open("math/math1.5.2(1).png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="-")
            photo = open("math/math1.5.2(2).png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.5.3":
            photo = open("math/math1.5.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.6.1":
            photo = open("math/math1.6.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.6.2":
            photo = open("math/math1.6.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.6.3":
            photo = open("math/math1.6.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.6.4":
            photo = open("math/math1.6.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "1.7.1":
            photo = open("math/math1.7.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.7.2":
            photo = open("math/math1.7.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.7.3":
            photo = open("math/math1.7.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.7.4":
            photo = open("math/math1.7.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "1.8.1":
            photo = open("math/math1.8.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.8.2":
            photo = open("math/math1.8.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.8.3":
            photo = open("math/math1.8.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.8.4":
            photo = open("math/math1.8.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")
        elif call.data == "1.10.1":
            photo = open("math/math1.10.1.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 1")
        elif call.data == "1.10.2":
            photo = open("math/math1.10.2.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 2")
        elif call.data == "1.10.3":
            photo = open("math/math1.10.3.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 3")
        elif call.data == "1.10.4":
            photo = open("math/math1.10.4.png", "rb")
            bot.send_photo(call.message.chat.id, photo, caption="مثال 4")


    # التأكد من تعيين callback_data لجميع الأمثلة في كل درس بطريقة مشابهة لبقية الدروس.

bot.polling()
