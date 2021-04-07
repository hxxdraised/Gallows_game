import telebot
import pickle

import bot_config as config
from telebot import types
import random as rand
# from csv_reader import Reader
import reader

bot = telebot.TeleBot(config.TOKEN)  # считывание токена
print(config.TOKEN)

words = {}
score = {}
start_game = {}
mistake_counter = {}
word = {}
hint = {}
hidden_word = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    global score
    global start_game
    global mistake_counter
    global words
    global word
    global hint
    global hidden_word

    words.update({message.chat.id: []})
    score.update({message.chat.id: [0, 0]})
    start_game.update({message.chat.id: False})
    mistake_counter.update({message.chat.id: 0})
    word.update({message.chat.id: ""})
    hint.update({message.chat.id: ""})
    hidden_word.update({message.chat.id: []})

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton(" ⬇️ Начать игру ", callback_data='start')
    item2 = types.InlineKeyboardButton(" ℹ️ Правила ", callback_data='rules')
    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     """Добро пожаловать, {0.first_name}!\nЭто бот-версия игры <b>"Виселица"</b>""".format(
                         message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global score
    global start_game
    global mistake_counter
    global words
    global word
    global hint
    global hidden_word

    try:
        if call.message:
            if call.data == 'rules':

                bot.answer_callback_query(callback_query_id=call.id)
                bot.send_message(call.message.chat.id, reader.read_rules())

            elif call.data == 'start':

                bot.answer_callback_query(callback_query_id=call.id)

                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("Легкая", callback_data='lvl_0')
                item2 = types.InlineKeyboardButton("Нормальная", callback_data='lvl_1')
                item3 = types.InlineKeyboardButton("Сложная", callback_data='lvl_2')
                markup.add(item1, item2, item3)

                bot.send_message(call.message.chat.id, "Выберите сложность: ", reply_markup=markup)


            elif call.data == 'lvl_0':

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Игра началась")

                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                words[call.message.chat.id] = reader.read_words(
                    0)  # считывание слов и подсказок для дальнейшего использования
                start_game[call.message.chat.id] = True
                mistake_counter[call.message.chat.id] = 0
                word_index = rand.randint(0, len(words[call.message.chat.id]) - 1)
                word[call.message.chat.id] = words[call.message.chat.id][word_index][0]
                hint[call.message.chat.id] = " ".join(words[call.message.chat.id][word_index][1::])
                hidden_word[call.message.chat.id] = ["_" for i in range(len(word[call.message.chat.id]))]
                bot.send_message(call.message.chat.id, "...::: Слово загадано :::...")
                word_output(call.message)

            elif call.data == 'lvl_1':

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Игра началась")

                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                words[call.message.chat.id] = reader.read_words(
                    1)  # считывание слов и подсказок для дальнейшего использования
                start_game[call.message.chat.id] = True
                mistake_counter[call.message.chat.id] = 0
                word_index = rand.randint(0, len(words[call.message.chat.id]) - 1)
                word[call.message.chat.id] = words[call.message.chat.id][word_index][0]
                hint[call.message.chat.id] = " ".join(words[call.message.chat.id][word_index][1::])
                hidden_word[call.message.chat.id] = ["_" for i in range(len(word[call.message.chat.id]))]
                bot.send_message(call.message.chat.id, "...::: Слово загадано :::...")
                word_output(call.message)

            elif call.data == 'lvl_2':

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Игра началась")

                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

                words[call.message.chat.id] = reader.read_words(
                    2)  # считывание слов и подсказок для дальнейшего использования
                start_game[call.message.chat.id] = True
                mistake_counter[call.message.chat.id] = 0
                word_index = rand.randint(0, len(words[call.message.chat.id]) - 1)
                word[call.message.chat.id] = words[call.message.chat.id][word_index][0]
                hint[call.message.chat.id] = " ".join(words[call.message.chat.id][word_index][1::])
                hidden_word[call.message.chat.id] = ["_" for i in range(len(word[call.message.chat.id]))]
                bot.send_message(call.message.chat.id, "...::: Слово загадано :::...")
                word_output(call.message)

            elif call.data == 'end':

                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Вы сдались")

                score[call.message.chat.id][1] += 1
                sticker = open('stickers/8.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sticker)

                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton(" Играть еще раз ", callback_data='start')
                markup.add(item)

                bot.send_message(call.message.chat.id, "...::: Вы закончили игру :| :::... \nЗагаданное слово: " + str(
                    word[call.message.chat.id]))
                bot.send_message(call.message.chat.id, " ✅ Слов отгадано: " + str(
                    score[call.message.chat.id][0]) + "\n❌ Неудачных попыток: " + str(score[call.message.chat.id][1]),
                                 reply_markup=markup)
                start_game[call.message.chat.id] = False

    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def letter_check(message):
    global score
    global mistake_counter
    global hidden_word
    global start_game

    if (message.chat.type == 'private'):
        if (start_game[message.chat.id]):

            letter = message.text  # считываем букву
            letter = letter.lower()  # убираем чувствительность к регистру

            if letter in word[message.chat.id]:
                if letter not in hidden_word[message.chat.id]:
                    for letter_index in range(len(word[message.chat.id])):
                        if word[message.chat.id][letter_index] == letter:
                            hidden_word[message.chat.id][letter_index] = letter
                    bot.send_message(message.chat.id, "Да, такая буква есть в слове 😌")
                else:
                    bot.send_message(message.chat.id, "Вы уже проверяли эту букву! 😠")
            else:
                bot.send_message(message.chat.id, "К сожалению, такой буквы нет в слове 🤭")
                mistake_counter[message.chat.id] += 1

            if mistake_counter[message.chat.id] > 7:
                score[message.chat.id][1] += 1
                sticker = open('stickers/8.webp', 'rb')
                bot.send_sticker(message.chat.id, sticker)

                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton(" Играть еще раз ", callback_data='start')
                markup.add(item)

                bot.send_message(message.chat.id,
                                 "...::: Вы проиграли :( :::... \nЗагаданное слово: " + str(word[message.chat.id]))
                bot.send_message(message.chat.id, " ✅ Слов отгадано: " + str(
                    score[message.chat.id][0]) + "\n❌ Неудачных попыток: " + str(score[message.chat.id][1]),
                                 reply_markup=markup)
                start_game[message.chat.id] = False

            elif "_" in hidden_word[message.chat.id]:
                word_output(message)

            else:
                score[message.chat.id][0] += 1

                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton(" Играть еще раз ", callback_data='start')
                markup.add(item)

                bot.send_message(message.chat.id, "...::: Слово отгадано :::... \nЗагаданное слово: " + str(
                    word[message.chat.id]) + "\nОшибок за игру: " + str(mistake_counter[message.chat.id]))
                bot.send_message(message.chat.id, " ✅ Слов отгадано: " + str(
                    score[message.chat.id][0]) + "\n❌ Неудачных попыток: " + str(score[message.chat.id][1]),
                                 reply_markup=markup)
                start_game[message.chat.id] = False

        else:
            bot.send_message(message.chat.id, "Начните игру!")


def word_output(message):
    sticker = open('stickers/{}.webp'.format(mistake_counter[message.chat.id]), 'rb')
    bot.send_sticker(message.chat.id, sticker)

    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(" Я сдаюсь 😕 ", callback_data='end')
    markup.add(item)

    bot.send_message(message.chat.id,
                     "<b>" + ' '.join(hidden_word[message.chat.id]) + "</b>" + "\n👉 Подсказка: " + str(
                         hint[message.chat.id]), parse_mode="html", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
