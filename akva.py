################################################
# """___________________Аква________________"""#
################################################

import telebot
import logging

from telebot import types

logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot("5632303879:AAHiEDgdAP7iFtudfBUOj7CkuA2kS_d6imI")  # токен


############################################################
# """_______________________Старт_______________________"""#
############################################################

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    # "___Фото__"
    sto = open('аква3.jpg', 'rb')  # Вступительное фото
    bot.send_photo(message.chat.id, sto)

    # "___Клавиатура___"
    clav = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tp1 = types.KeyboardButton("Помолица🙏")  # Кнопка 1
    tp2 = types.KeyboardButton("Пожертвовать богине 💸")  # Кнопка 2
    clav.add(tp1, tp2)

    # "___Привецтвие___"
    bot.send_message(message.chat.id,
                     "Добро пожаловать прихожанин, {0.first_name}! \n "
                     "Я - <b>храм Аквы</b>, бот храм созданный для того, чтобы служить и восхвалять прекрасную богиню Акву.".format(
                         message.from_user, ), parse_mode='html', reply_markup=clav)


#############################################################
# ""_____________________Обычные Кнопки___________________""#
#############################################################

@bot.message_handler(content_types=['text'])
def lop(message):
    # "___Фото___"
    cop_1 = open('аква1.jpg', 'rb')  # Фото иконы №1
    cop_2 = open('аква2.jpg', 'rb')  # Фото иконы №2
    cop_3 = open('аква4.jpg', 'rb')  # Фото иконы №3
    cop_4 = open('sticker2.webp', 'rb')  # Стикер пожертвувание

    if message.chat.type == 'private':

        # ""_____Помолица_____""
        if message.text == 'Помолица🙏':
            kls = types.InlineKeyboardMarkup(row_width=1)  # клавиатура номер два

            bot.send_photo(message.chat.id, cop_1)  # Иконы для молитвы
            bot.send_photo(message.chat.id, cop_2)  # вторая икона для молитвы
            bot.send_photo(message.chat.id, cop_3)  # третя икона для молитвы

            itm = types.InlineKeyboardButton("Помолица", callback_data='good')  # Значение клавиатура номер два

            kls.add(itm)  # Клавиатура номер два

            bot.send_message(message.chat.id, str("О великая Аква благослови меня и дай мне сил \n"
                                                  "Даруй мне удачу пройти данж, и отведи от меня проклятых мобов \n"
                                                  "Даруй большую награду, и понизь статы нечестивого боса \n"
                                                  "Помоги выкрутить легендарку повысь коэффициент \n"
                                                  "АКВАААААААААААААААААААААААА \n"
                                                  "🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏"),
                             reply_markup=kls)  # Ответ на кнопку помалица Молитва

        # ""_____Пожертвовать 💳_____""
        elif message.text == 'Пожертвовать богине 💸':  # Пожертвувание

            kls2 = types.InlineKeyboardMarkup(row_width=1)  # Клавиатура с сылкой
            itm2 = types.InlineKeyboardButton("пожертвовать дзвонкую монетку ",
                                              callback_data='lom')  # Клавиатура с сылкой
            kls2.add(itm2)  # Клавиатура с сылкой

            bot.send_sticker(message.chat.id, cop_4)  # Стикер пожертв №1
            # Оплата
            bot.send_message(message.chat.id, text="Пожертвуй Акве монетку для выплаты долгов \n"
                                                   " И на бутылочку пивка", reply_markup=kls2)  # текст пожертвы

            # ""______Если напишут того чого нету в командах ______""
        else:
            bot.send_message(message.chat.id,
                             "Пишы правельно ЕРИТИК!!!!!!")  # на случай если воспользуюце не клавиатурой


####################################################################
# ""_____________________Инлайновая клавиатура___________________""#
####################################################################

@bot.callback_query_handler(lambda query: True)
def callback_inline(call):
    try:
        if call.message:

            # ""______Помолица______""
            if call.data == 'good':
                cop_3 = open('sticker.webp', 'rb')
                bot.send_sticker(call.message.chat.id, cop_3)
                bot.send_message(call.message.chat.id, 'Грех отпущен')  # после нажатия текст
                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="Молитва окончена",
                                      reply_markup=None)  # замена кнопки инлайтовой клавиатуры
                bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=False,
                                          text="Грех отпущен !!!!")  # Оповищение

                # ""______Пожертвовать______""
            elif call.data == 'lom':

                cop_5 = open('sticker3.webp', 'rb')
                cop_6 = open('sticker4.webp', 'rb')

                bot.send_sticker(call.message.chat.id, cop_5)  # Стикер после оплаты №1
                bot.send_sticker(call.message.chat.id, cop_6)  # Стикер после оплаты №2
                bot.send_message(call.message.chat.id,
                                 text="Большое спасибо семпай, теперь я смогу отдать долг \n"
                                      "И выпить бутылочку вина ❤")

                bot.send_message(call.message.chat.id, 'https://prt.mn/k_sJ_1O66x')  # после нажатия текст

                bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text='Спасибо 🥰',
                                      reply_markup=None)  # замена кнопки инлайтовой клавиатуры

                bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=False,
                                          text="❤️❤️❤️❤️❤️")  # Оповищение
        # "___Поиск ошыбок___"
    except Exception as e:
        print(repr(e))  # Поиск ощыбок


try:
    if __name__ == "__main__":
        print("Бот запущен проблем нет")
        bot.polling(none_stop=True)
except Exception as _ex:
    print("Ошыбка")