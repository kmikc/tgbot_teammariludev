#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, KeyboardButton
from telegram.ext import Updater, CommandHandler, Job, CallbackQueryHandler, ConversationHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from pydrive.auth import GoogleAuth
import sqlite3 as lite
from time import mktime
from datetime import datetime, timedelta
from unicodedata import normalize

def settings_menu(bot, update):
    keyboard = [
        [
            InlineKeyboardButton('Configurar timezone', callback_data='set_timezone')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Seleccion opción a configurar:', reply_markup=reply_markup)


def settings_timezone(bot, update, query):

    print "settings_timezone"

    if query.data == 'set_timezone':
        keyboard =  [
            [InlineKeyboardButton("Africa", callback_data='TIMEZONE_CONTINUE:Africa'), InlineKeyboardButton("America", callback_data='TIMEZONE_CONTINUE:America'), InlineKeyboardButton("Asia", callback_data='TIMEZONE_CONTINUE:Asia'), InlineKeyboardButton("Australia", callback_data='TIMEZONE_CONTINUE:Australia')],
            [InlineKeyboardButton("Europe", callback_data='TIMEZONE_CONTINUE:Europe'), InlineKeyboardButton("Indian", callback_data='TIMEZONE_CONTINUE:Indian'), InlineKeyboardButton("Pacific", callback_data='TIMEZONE_CONTINUE:Pacific')]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Africa':
        keyboard = [
            [InlineKeyboardButton('Abidjan', callback_data='TIMEZONE_SAVE:Africa/Abidjan')],
            [InlineKeyboardButton('Accra', callback_data='TIMEZONE_SAVE:Africa/Accra')],
            [InlineKeyboardButton('Addis_Ababa', callback_data='TIMEZONE_SAVE:Africa/Addis_Ababa')],
            [InlineKeyboardButton('Algiers', callback_data='TIMEZONE_SAVE:Africa/Algiers')],
            [InlineKeyboardButton('Asmara', callback_data='TIMEZONE_SAVE:Africa/Asmara')],
            [InlineKeyboardButton('Asmera', callback_data='TIMEZONE_SAVE:Africa/Asmera')],
            [InlineKeyboardButton('Bamako', callback_data='TIMEZONE_SAVE:Africa/Bamako')],
            [InlineKeyboardButton('Bangui', callback_data='TIMEZONE_SAVE:Africa/Bangui')],
            [InlineKeyboardButton('Banjul', callback_data='TIMEZONE_SAVE:Africa/Banjul')],
            [InlineKeyboardButton('Bissau', callback_data='TIMEZONE_SAVE:Africa/Bissau')],
            [InlineKeyboardButton('Blantyre', callback_data='TIMEZONE_SAVE:Africa/Blantyre')],
            [InlineKeyboardButton('Brazzaville', callback_data='TIMEZONE_SAVE:Africa/Brazzaville')],
            [InlineKeyboardButton('Bujumbura', callback_data='TIMEZONE_SAVE:Africa/Bujumbura')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'America':
        keyboard = [
            [InlineKeyboardButton('Adak', callback_data='TIMEZONE_SAVE:America/Adak')],
            [InlineKeyboardButton('Anchorage', callback_data='TIMEZONE_SAVE:America/Anchorage')],
            [InlineKeyboardButton('Anguilla', callback_data='TIMEZONE_SAVE:America/Anguilla')],
            [InlineKeyboardButton('Antigua', callback_data='TIMEZONE_SAVE:America/Antigua')],
            [InlineKeyboardButton('Araguaina', callback_data='TIMEZONE_SAVE:America/Araguaina')],
            [InlineKeyboardButton('Aruba', callback_data='TIMEZONE_SAVE:America/Aruba')],
            [InlineKeyboardButton('Asuncion', callback_data='TIMEZONE_SAVE:America/Asuncion')],
            [InlineKeyboardButton('Atikokan', callback_data='TIMEZONE_SAVE:America/Atikokan')],
            [InlineKeyboardButton('Atka', callback_data='TIMEZONE_SAVE:America/Atka')],
            [InlineKeyboardButton('Bahia', callback_data='TIMEZONE_SAVE:America/Bahia')],
            [InlineKeyboardButton('Bahia_Banderas', callback_data='TIMEZONE_SAVE:America/Bahia_Banderas')],
            [InlineKeyboardButton('Barbados', callback_data='TIMEZONE_SAVE:America/Barbados')],
            [InlineKeyboardButton('Belem', callback_data='TIMEZONE_SAVE:America/Belem')],
            [InlineKeyboardButton('Belize', callback_data='TIMEZONE_SAVE:America/Belize')],
            [InlineKeyboardButton('Blanc-Sablon', callback_data='TIMEZONE_SAVE:America/Blanc-Sablon')],
            [InlineKeyboardButton('Boa_Vista', callback_data='TIMEZONE_SAVE:America/Boa_Vista')],
            [InlineKeyboardButton('Bogota', callback_data='TIMEZONE_SAVE:America/Bogota')],
            [InlineKeyboardButton('Boise', callback_data='TIMEZONE_SAVE:America/Boise')],
            [InlineKeyboardButton('Buenos_Aires', callback_data='TIMEZONE_SAVE:America/Buenos_Aires')],
            [InlineKeyboardButton('Cambridge_Bay', callback_data='TIMEZONE_SAVE:America/Cambridge_Bay')],
            [InlineKeyboardButton('Campo_Grande', callback_data='TIMEZONE_SAVE:America/Campo_Grande')],
            [InlineKeyboardButton('Cancun', callback_data='TIMEZONE_SAVE:America/Cancun')],
            [InlineKeyboardButton('Caracas', callback_data='TIMEZONE_SAVE:America/Caracas')],
            [InlineKeyboardButton('Catamarca', callback_data='TIMEZONE_SAVE:America/Catamarca')],
            [InlineKeyboardButton('Cayenne', callback_data='TIMEZONE_SAVE:America/Cayenne')],
            [InlineKeyboardButton('Cayman', callback_data='TIMEZONE_SAVE:America/Cayman')],
            [InlineKeyboardButton('Chicago', callback_data='TIMEZONE_SAVE:America/Chicago')],
            [InlineKeyboardButton('Chihuahua', callback_data='TIMEZONE_SAVE:America/Chihuahua')],
            [InlineKeyboardButton('Coral_Harbour', callback_data='TIMEZONE_SAVE:America/Coral_Harbour')],
            [InlineKeyboardButton('Cordoba', callback_data='TIMEZONE_SAVE:America/Cordoba')],
            [InlineKeyboardButton('Costa_Rica', callback_data='TIMEZONE_SAVE:America/Costa_Rica')],
            [InlineKeyboardButton('Creston', callback_data='TIMEZONE_SAVE:America/Creston')],
            [InlineKeyboardButton('Cuiaba', callback_data='TIMEZONE_SAVE:America/Cuiaba')],
            [InlineKeyboardButton('Curacao', callback_data='TIMEZONE_SAVE:America/Curacao')],
            [InlineKeyboardButton('Danmarkshavn', callback_data='TIMEZONE_SAVE:America/Danmarkshavn')],
            [InlineKeyboardButton('Dawson', callback_data='TIMEZONE_SAVE:America/Dawson')],
            [InlineKeyboardButton('Dawson_Creek', callback_data='TIMEZONE_SAVE:America/Dawson_Creek')],
            [InlineKeyboardButton('Denver', callback_data='TIMEZONE_SAVE:America/Denver')],
            [InlineKeyboardButton('Detroit', callback_data='TIMEZONE_SAVE:America/Detroit')],
            [InlineKeyboardButton('Dominica', callback_data='TIMEZONE_SAVE:America/Dominica')],
            [InlineKeyboardButton('Edmonton', callback_data='TIMEZONE_SAVE:America/Edmonton')],
            [InlineKeyboardButton('Eirunepe', callback_data='TIMEZONE_SAVE:America/Eirunepe')],
            [InlineKeyboardButton('El_Salvador', callback_data='TIMEZONE_SAVE:America/El_Salvador')],
            [InlineKeyboardButton('Ensenada', callback_data='TIMEZONE_SAVE:America/Ensenada')],
            [InlineKeyboardButton('Fort_Wayne', callback_data='TIMEZONE_SAVE:America/Fort_Wayne')],
            [InlineKeyboardButton('Fortaleza', callback_data='TIMEZONE_SAVE:America/Fortaleza')],
            [InlineKeyboardButton('Glace_Bay', callback_data='TIMEZONE_SAVE:America/Glace_Bay')],
            [InlineKeyboardButton('Godthab', callback_data='TIMEZONE_SAVE:America/Godthab')],
            [InlineKeyboardButton('Goose_Bay', callback_data='TIMEZONE_SAVE:America/Goose_Bay')],
            [InlineKeyboardButton('Grand_Turk', callback_data='TIMEZONE_SAVE:America/Grand_Turk')],
            [InlineKeyboardButton('Grenada', callback_data='TIMEZONE_SAVE:America/Grenada')],
            [InlineKeyboardButton('Guadeloupe', callback_data='TIMEZONE_SAVE:America/Guadeloupe')],
            [InlineKeyboardButton('Guatemala', callback_data='TIMEZONE_SAVE:America/Guatemala')],
            [InlineKeyboardButton('Guayaquil', callback_data='TIMEZONE_SAVE:America/Guayaquil')],
            [InlineKeyboardButton('Guyana', callback_data='TIMEZONE_SAVE:America/Guyana')],
            [InlineKeyboardButton('Halifax', callback_data='TIMEZONE_SAVE:America/Halifax')],
            [InlineKeyboardButton('havana', callback_data='TIMEZONE_SAVE:America/havana')],
            [InlineKeyboardButton('Hermosillo', callback_data='TIMEZONE_SAVE:America/Hermosillo')],
            [InlineKeyboardButton('Indianapolis', callback_data='TIMEZONE_SAVE:America/Indianapolis')],
            [InlineKeyboardButton('Inuvik', callback_data='TIMEZONE_SAVE:America/Inuvik')],
            [InlineKeyboardButton('Iqaluit', callback_data='TIMEZONE_SAVE:America/Iqaluit')],
            [InlineKeyboardButton('Jamaica', callback_data='TIMEZONE_SAVE:America/Jamaica')],
            [InlineKeyboardButton('Jujuy', callback_data='TIMEZONE_SAVE:America/Jujuy')],
            [InlineKeyboardButton('Juneau', callback_data='TIMEZONE_SAVE:America/Juneau')],
            [InlineKeyboardButton('Knox_IN', callback_data='TIMEZONE_SAVE:America/Knox_IN')],
            [InlineKeyboardButton('Kralendijk', callback_data='TIMEZONE_SAVE:America/Kralendijk')],
            [InlineKeyboardButton('La_Paz', callback_data='TIMEZONE_SAVE:America/La_Paz')],
            [InlineKeyboardButton('Lima', callback_data='TIMEZONE_SAVE:America/Lima')],
            [InlineKeyboardButton('Los_Angeles', callback_data='TIMEZONE_SAVE:America/Los_Angeles')],
            [InlineKeyboardButton('Louisville', callback_data='TIMEZONE_SAVE:America/Louisville')],
            [InlineKeyboardButton('Maceio', callback_data='TIMEZONE_SAVE:America/Maceio')],
            [InlineKeyboardButton('Managua', callback_data='TIMEZONE_SAVE:America/Managua')],
            [InlineKeyboardButton('Manaus', callback_data='TIMEZONE_SAVE:America/Manaus')],
            [InlineKeyboardButton('Marigot', callback_data='TIMEZONE_SAVE:America/Marigot')],
            [InlineKeyboardButton('Martinique', callback_data='TIMEZONE_SAVE:America/Martinique')],
            [InlineKeyboardButton('Matamoros', callback_data='TIMEZONE_SAVE:America/Matamoros')],
            [InlineKeyboardButton('Mazatlan', callback_data='TIMEZONE_SAVE:America/Mazatlan')],
            [InlineKeyboardButton('Mendoza', callback_data='TIMEZONE_SAVE:America/Mendoza')],
            [InlineKeyboardButton('Menominee', callback_data='TIMEZONE_SAVE:America/Menominee')],
            [InlineKeyboardButton('Merida', callback_data='TIMEZONE_SAVE:America/Merida')],
            [InlineKeyboardButton('Metlakatla', callback_data='TIMEZONE_SAVE:America/Metlakatla')],
            [InlineKeyboardButton('Mexico_City', callback_data='TIMEZONE_SAVE:America/Mexico_City')],
            [InlineKeyboardButton('Miquelon', callback_data='TIMEZONE_SAVE:America/Miquelon')],
            [InlineKeyboardButton('Moncton', callback_data='TIMEZONE_SAVE:America/Moncton')],
            [InlineKeyboardButton('Monterrey', callback_data='TIMEZONE_SAVE:America/Monterrey')],
            [InlineKeyboardButton('Montevideo', callback_data='TIMEZONE_SAVE:America/Montevideo')],
            [InlineKeyboardButton('Montreal', callback_data='TIMEZONE_SAVE:America/Montreal')],
            [InlineKeyboardButton('Montserrat', callback_data='TIMEZONE_SAVE:America/Montserrat')],
            [InlineKeyboardButton('Nassau', callback_data='TIMEZONE_SAVE:America/Nassau')],
            [InlineKeyboardButton('New_York', callback_data='TIMEZONE_SAVE:America/New_York')],
            [InlineKeyboardButton('Nipigon', callback_data='TIMEZONE_SAVE:America/Nipigon')],
            [InlineKeyboardButton('Nome', callback_data='TIMEZONE_SAVE:America/Nome')],
            [InlineKeyboardButton('Noronha', callback_data='TIMEZONE_SAVE:America/Noronha')],
            [InlineKeyboardButton('Ojinaga', callback_data='TIMEZONE_SAVE:America/Ojinaga')],
            [InlineKeyboardButton('Panama', callback_data='TIMEZONE_SAVE:America/Panama')],
            [InlineKeyboardButton('Lower_Princes', callback_data='TIMEZONE_SAVE:America/Lower_Princes')],
            [InlineKeyboardButton('Pangnirtung', callback_data='TIMEZONE_SAVE:America/Pangnirtung')],
            [InlineKeyboardButton('Paramaribo', callback_data='TIMEZONE_SAVE:America/Paramaribo')],
            [InlineKeyboardButton('Phoenix', callback_data='TIMEZONE_SAVE:America/Phoenix')],
            [InlineKeyboardButton('Port-au-Prince', callback_data='TIMEZONE_SAVE:America/Port-au-Prince')],
            [InlineKeyboardButton('Port_of_Spain', callback_data='TIMEZONE_SAVE:America/Port_of_Spain')],
            [InlineKeyboardButton('Porto_Acre', callback_data='TIMEZONE_SAVE:America/Porto_Acre')],
            [InlineKeyboardButton('Porto_Velho', callback_data='TIMEZONE_SAVE:America/Porto_Velho')],
            [InlineKeyboardButton('Puerto_Rico', callback_data='TIMEZONE_SAVE:America/Puerto_Rico')],
            [InlineKeyboardButton('Rainy_River', callback_data='TIMEZONE_SAVE:America/Rainy_River')],
            [InlineKeyboardButton('Rankin_Inlet', callback_data='TIMEZONE_SAVE:America/Rankin_Inlet')],
            [InlineKeyboardButton('Recife', callback_data='TIMEZONE_SAVE:America/Recife')],
            [InlineKeyboardButton('Regina', callback_data='TIMEZONE_SAVE:America/Regina')],
            [InlineKeyboardButton('Resolute', callback_data='TIMEZONE_SAVE:America/Resolute')],
            [InlineKeyboardButton('Rio_Branco', callback_data='TIMEZONE_SAVE:America/Rio_Branco')],
            [InlineKeyboardButton('Rosario', callback_data='TIMEZONE_SAVE:America/Rosario')],
            [InlineKeyboardButton('Santa_Isabel', callback_data='TIMEZONE_SAVE:America/Santa_Isabel')],
            [InlineKeyboardButton('Santarem', callback_data='TIMEZONE_SAVE:America/Santarem')],
            [InlineKeyboardButton('Santiago', callback_data='TIMEZONE_SAVE:America/Santiago')],
            [InlineKeyboardButton('Santo_Domingo', callback_data='TIMEZONE_SAVE:America/Santo_Domingo')],
            [InlineKeyboardButton('Sao_Paulo', callback_data='TIMEZONE_SAVE:America/Sao_Paulo')],
            [InlineKeyboardButton('Scoresbysund', callback_data='TIMEZONE_SAVE:America/Scoresbysund')],
            [InlineKeyboardButton('Shiprock', callback_data='TIMEZONE_SAVE:America/Shiprock')],
            [InlineKeyboardButton('Sitka', callback_data='TIMEZONE_SAVE:America/Sitka')],
            [InlineKeyboardButton('St_Barthelemy', callback_data='TIMEZONE_SAVE:America/St_Barthelemy')],
            [InlineKeyboardButton('St_Johns', callback_data='TIMEZONE_SAVE:America/St_Johns')],
            [InlineKeyboardButton('St_Kitts', callback_data='TIMEZONE_SAVE:America/St_Kitts')],
            [InlineKeyboardButton('St_Lucia', callback_data='TIMEZONE_SAVE:America/St_Lucia')],
            [InlineKeyboardButton('St_Thomas', callback_data='TIMEZONE_SAVE:America/St_Thomas')],
            [InlineKeyboardButton('St_Vincent', callback_data='TIMEZONE_SAVE:America/St_Vincent')],
            [InlineKeyboardButton('Swift_Current', callback_data='TIMEZONE_SAVE:America/Swift_Current')],
            [InlineKeyboardButton('Tegucigalpa', callback_data='TIMEZONE_SAVE:America/Tegucigalpa')],
            [InlineKeyboardButton('Thule', callback_data='TIMEZONE_SAVE:America/Thule')],
            [InlineKeyboardButton('Thunder_Bay', callback_data='TIMEZONE_SAVE:America/Thunder_Bay')],
            [InlineKeyboardButton('Tijuana', callback_data='TIMEZONE_SAVE:America/Tijuana')],
            [InlineKeyboardButton('Toronto', callback_data='TIMEZONE_SAVE:America/Toronto')],
            [InlineKeyboardButton('Tortola', callback_data='TIMEZONE_SAVE:America/Tortola')],
            [InlineKeyboardButton('Vancouver', callback_data='TIMEZONE_SAVE:America/Vancouver')],
            [InlineKeyboardButton('Virgin', callback_data='TIMEZONE_SAVE:America/Virgin')],
            [InlineKeyboardButton('Whitehorse', callback_data='TIMEZONE_SAVE:America/Whitehorse')],
            [InlineKeyboardButton('Winnipeg', callback_data='TIMEZONE_SAVE:America/Winnipeg')],
            [InlineKeyboardButton('Yakutat', callback_data='TIMEZONE_SAVE:America/Yakutat')],
            [InlineKeyboardButton('Yellowknife', callback_data='TIMEZONE_SAVE:America/Yellowknife')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Asia':

        keyboard = [
            [InlineKeyboardButton('Aden', callback_data='TIMEZONE_SAVE:Asia/Aden')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Australia':

        keyboard = [
            [InlineKeyboardButton('Adelaide', callback_data='TIMEZONE_SAVE:Australia/Adelaide')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Europe':

        keyboard = [
            [InlineKeyboardButton('Amsterdam', callback_data='TIMEZONE_SAVE:Europe/Amsterdam')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Indian':

        keyboard = [
            [InlineKeyboardButton('Antananarivo', callback_data='TIMEZONE_SAVE:Indian/Antananarivo')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    elif query.data == 'Pacific':

        keyboard = [
            [InlineKeyboardButton('Apia', callback_data='TIMEZONE_SAVE:Pacific/Apia')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)


def settings0(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id, text='settings...')
    settings1(bot, update)


def settings1(bot, update):
    keyboard =  [
                    [InlineKeyboardButton("Africa", callback_data='Africa'), InlineKeyboardButton("America", callback_data='America'), InlineKeyboardButton("Asia", callback_data='Asia'), InlineKeyboardButton("Australia", callback_data='Australia')],
                    [InlineKeyboardButton("Europe", callback_data='Europe'), InlineKeyboardButton("Indian", callback_data='Indian'), InlineKeyboardButton("Pacific", callback_data='Pacific')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Configurando zona horaria:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    if (data == 'set_timezone') or (data == 'Africa') or (data == 'America') or (data == 'Asia') or (data == 'Australia') or (data == 'Europe') or (data == 'Indian') or (data == 'Pacific'):
        settings_timezone(bot, update, query)

    else:
        bot.editMessageText(text=format(query), chat_id=chat_id, message_id=message_id)


def get_chat_timezone(p_chat_id):
    query = "SELECT timezone FROM chat_settings WHERE chat_id={CHATID};".format(CHATID=p_chat_id)

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
    update.message.reply_text('Hola {}'.format(update.message.from_user.first_name))


def teammarilu(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id, text='Invocan a @Rottenman @victorono @MalKarakter')


def drive(bot, update):
    gauth = GoogleAuth()
    auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
    code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
    gauth.Auth(code) # Authorize and build service from the code


def get_gmt(p_chat_id, p_chat_title, p_chat_username):
    update.message.reply_text('get_gmt...')
    conn = lite.connect('checkpoint_settings.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM chat_gmt WHERE chat_id=:CHATID", {"CHATID": p_chat_id})
    gmt_value_count = cur.fetchone()[0]
    if gmt_value_count > 0:
        cur.execute("SELECT gmt_value FROM chat_gmt WHERE chat_id=:CHATID", {"CHATID": p_chat_id})
        gmt_value = cur.fetchone()[0]
    else:
        gmt_value = 0
        cur.execute("INSERT INTO chat_gmt (chat_id, gmt_value) VALUES (?, ?)", (p_chat_id, gmt_value))
        conn.commit()

    cur.execute("UPDATE chat_gmt SET chat_title=? , chat_username=? , datetime=datetime(CURRENT_TIMESTAMP, 'localtime') WHERE chat_id=?", (p_chat_title, p_chat_username, p_chat_id))
    conn.commit()
    conn.close()

    update.message.reply_text(gmt_value)

    return gmt_value


def checkpoints(bot, update):
    update.message.reply_text(format(update.message.chat))
    chatid = update.message.chat.id
    chattitle = update.message.chat.title
    chatusername = update.message.chat.username
    gmt_value = get_gmt(chatid, chattitle, chatusername)

    t0 = datetime.strptime('2014-07-09 15', '%Y-%m-%d %H') + timedelta(hours=gmt_value)
    hours_per_cycle = 175

    t = datetime.now()

    seconds = mktime(t.timetuple()) - mktime(t0.timetuple())
    cycles = seconds // (3600 * hours_per_cycle)
    start = t0 + timedelta(hours=cycles * hours_per_cycle)
    checkpoints = map(lambda x: start + timedelta(hours=x), range(0, hours_per_cycle, 5))
    nextcp_mark = False

    acheckpoints = []
    for num, checkpoint in enumerate(checkpoints):

        if checkpoint > t and nextcp_mark == False:
            str_checkpoint = format(str(checkpoint)) + ' <---'
            nextcp_mark = True
        else:
            str_checkpoint = format(str(checkpoint))

        acheckpoints.append(str_checkpoint)

    res = ' \n '.join(acheckpoints)
    update.message.reply_text(res)


def notify_checkpoint(bot, job):
    bot.sendMessage(chat_id=37307558, text='Oli')


def test_location(bot, update):
    print "test_location"
    #print bot
    #print update
    chat_id = update.message.chat.id
    location_keyboard = KeyboardButton(text="Enviar ubicación", request_location=True)
    #contact_keyboard = KeyboardButton(text="send_contact", request_contact=True)
    #custom_keyboard = [[ location_keyboard, contact_keyboard ]]
    custom_keyboard = [[ location_keyboard ]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=chat_id, text="Esperando ubicación", reply_markup=reply_markup)
    reply_markup = ReplyKeyboardHide()
    bot.sendMessage(chat_id=chat_id, text="Tiene que ir un texto", reply_markup=reply_markup)

tk = open('token').read().rstrip('\n')
updater = Updater(tk)

updater.dispatcher.add_handler(CommandHandler('info', start))
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('teammarilu', teammarilu))
updater.dispatcher.add_handler(CommandHandler('drive', drive))
updater.dispatcher.add_handler(CommandHandler('checkpoints', checkpoints))
updater.dispatcher.add_handler(CommandHandler('settings', settings_menu))
updater.dispatcher.add_handler(CommandHandler('test_location', test_location))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

#jobqueue = updater.job_queue
#checkpoint_queue = Job(notify_checkpoint, 10.0)
#jobqueue.put(checkpoint_queue, next_t=5.0)

updater.start_polling()
updater.idle()
