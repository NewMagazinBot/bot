import telebot
import const
from telebot import types

bot = telebot.TeleBot(const.API_TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_address = types.KeyboardButton('Доступные районы')
btn_contact = types.KeyboardButton('Контакты')
btn_info = types.KeyboardButton('Информация')
btn_payment = types.KeyboardButton('Способы оплаты')

markup_menu.add(btn_address, btn_contact, btn_info, btn_payment)

markup_inline_address = types.InlineKeyboardMarkup()
btn_in_avg = types.InlineKeyboardButton("м.23 августа", callback_data="avg")
btn_in_sad = types.InlineKeyboardButton("м.Бот сад", callback_data="sad")
btn_in_nau = types.InlineKeyboardButton("м.Научная", callback_data="nau")
btn_in_der = types.InlineKeyboardButton("м.Держпром", callback_data="der")

markup_inline_address.add(btn_in_avg, btn_in_sad, btn_in_nau, btn_in_der)

markup_inline_ves = types.InlineKeyboardMarkup()
btn_in_chek = types.InlineKeyboardButton('0.25 грамм', callback_data="chek")
btn_in_polka = types.InlineKeyboardButton('0,5 грамм', callback_data="polka")
btn_in_gram = types.InlineKeyboardButton('1 грамм', callback_data="gram")
markup_inline_ves.add(btn_in_chek, btn_in_polka, btn_in_gram)


@bot.message_handler(commands=['start'])
def send_welkome(message):
    bot.reply_to(message, "Привет, для начала прочитай информацию", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Доступные районы':
        bot.reply_to(message, "На сегодня доступные районы", reply_markup=markup_inline_address)
    elif message.text == "Контакты":
        bot.reply_to(message, "Связь с оператором с 10-00 до 00-00, @megashopkh", reply_markup=markup_menu)
    elif message.text == "Информация":
        bot.reply_to(message, "Для заказа, получения кошелька, подтверждения заказа пишите оператору,"
                              " все клады свежайшие, на сегодня в наличии только 0.25,"
                              " в ближайшее время появятся больше районов а также полная автоматика в боте",
                     reply_markup=markup_menu)
    elif message.text == "Способы оплаты":
        bot.reply_to(message, "Оплата принимается на кошелек EasyPay, для получения кошелька а также подтверждения"
                              "оплаты пишите оператору, цена 0,25грамм 600грн", reply_markup=markup_menu)

bot.polling()
