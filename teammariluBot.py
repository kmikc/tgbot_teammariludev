#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler
import sqlite3 as lite


def get_chat_timezone(p_chat_id):
    query = "SELECT timezone FROM chat_settings WHERE chat_id={CHATID};".\
        format(CHATID=p_chat_id)

    conn = lite.connect('checkpoint_settings.db')
    cur = conn.cursor()
    cur.execute(query)
    str_timezone = cur.fetchone()

    str_timezone = str_timezone[0]
    conn.commit()
    conn.close()

    return str_timezone


def start(bot, update):
    chat_id = update.message.chat.id
    update.message.reply_text(get_chat_timezone(chat_id))


def hello(bot, update):
    update.message.reply_text('Hola {}'.
                              format(update.message.from_user.first_name))


def teammarilu(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id,
                    text='Invocan a @Rottenman @victorono @MalKarakter')


def test_location(bot, update):
    print("test_location")
    chat_id = update.message.chat.id
    location_keyboard = telegram.KeyboardButton(
        text="send_location", request_location=True)
    custom_keyboard = [[location_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(
        chat_id=chat_id,
        text="Enviar ubicación actual",
        reply_markup=reply_markup)


tk = open('token').read().rstrip('\n')
updater = Updater(tk)
updater = Updater('189612249:AAFRvgiS71TiU6mb6Pu_nf0gVHmNMdc-8h0')

updater.dispatcher.add_handler(CommandHandler('info', start))
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('teammarilu', teammarilu))
updater.dispatcher.add_handler(CommandHandler('test_location', test_location))

# jobqueue = updater.job_queue
# checkpoint_queue = Job(notify_checkpoint, 10.0)
# jobqueue.put(checkpoint_queue, next_t=5.0)

updater.start_polling()
updater.idle()
