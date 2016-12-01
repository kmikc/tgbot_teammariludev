#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide
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
            [InlineKeyboardButton('Adak', callback_data='TIMEZONE_SAVE:Adak')],
            [InlineKeyboardButton('Anchorage', callback_data='TIMEZONE_SAVE:Anchorage')],
            [InlineKeyboardButton('Anguilla', callback_data='TIMEZONE_SAVE:Anguilla')],
            [InlineKeyboardButton('Antigua', callback_data='TIMEZONE_SAVE:Antigua')],
            [InlineKeyboardButton('Araguaina', callback_data='TIMEZONE_SAVE:Araguaina')],
            [InlineKeyboardButton('Aruba', callback_data='TIMEZONE_SAVE:Aruba')],
            [InlineKeyboardButton('Asuncion', callback_data='TIMEZONE_SAVE:Asuncion')],
            [InlineKeyboardButton('Atikokan', callback_data='TIMEZONE_SAVE:Atikokan')],
            [InlineKeyboardButton('Atka', callback_data='TIMEZONE_SAVE:Atka')],
            [InlineKeyboardButton('Bahia', callback_data='TIMEZONE_SAVE:Bahia')],
            [InlineKeyboardButton('Bahia_Banderas', callback_data='TIMEZONE_SAVE:Bahia_Banderas')],
            [InlineKeyboardButton('Barbados', callback_data='TIMEZONE_SAVE:Barbados')],
            [InlineKeyboardButton('Belem', callback_data='TIMEZONE_SAVE:Belem')],
            [InlineKeyboardButton('Belize', callback_data='TIMEZONE_SAVE:Belize')],
            [InlineKeyboardButton('Blanc-Sablon', callback_data='TIMEZONE_SAVE:Blanc-Sablon')],
            [InlineKeyboardButton('Boa_Vista', callback_data='TIMEZONE_SAVE:Boa_Vista')],
            [InlineKeyboardButton('Bogota', callback_data='TIMEZONE_SAVE:Bogota')],
            [InlineKeyboardButton('Boise', callback_data='TIMEZONE_SAVE:Boise')],
            [InlineKeyboardButton('Buenos_Aires', callback_data='TIMEZONE_SAVE:Buenos_Aires')],
            [InlineKeyboardButton('Cambridge_Bay', callback_data='TIMEZONE_SAVE:Cambridge_Bay')],
            [InlineKeyboardButton('Campo_Grande', callback_data='TIMEZONE_SAVE:Campo_Grande')],
            [InlineKeyboardButton('Cancun', callback_data='TIMEZONE_SAVE:Cancun')],
            [InlineKeyboardButton('Caracas', callback_data='TIMEZONE_SAVE:Caracas')],
            [InlineKeyboardButton('Catamarca', callback_data='TIMEZONE_SAVE:Catamarca')],
            [InlineKeyboardButton('Cayenne', callback_data='TIMEZONE_SAVE:Cayenne')],
            [InlineKeyboardButton('Cayman', callback_data='TIMEZONE_SAVE:Cayman')],
            [InlineKeyboardButton('Chicago', callback_data='TIMEZONE_SAVE:Chicago')],
            [InlineKeyboardButton('Chihuahua', callback_data='TIMEZONE_SAVE:Chihuahua')],
            [InlineKeyboardButton('Coral_Harbour', callback_data='TIMEZONE_SAVE:Coral_Harbour')],
            [InlineKeyboardButton('Cordoba', callback_data='TIMEZONE_SAVE:Cordoba')],
            [InlineKeyboardButton('Costa_Rica', callback_data='TIMEZONE_SAVE:Costa_Rica')],
            [InlineKeyboardButton('Creston', callback_data='TIMEZONE_SAVE:Creston')],
            [InlineKeyboardButton('Cuiaba', callback_data='TIMEZONE_SAVE:Cuiaba')],
            [InlineKeyboardButton('Curacao', callback_data='TIMEZONE_SAVE:Curacao')],
            [InlineKeyboardButton('Danmarkshavn', callback_data='TIMEZONE_SAVE:Danmarkshavn')],
            [InlineKeyboardButton('Dawson', callback_data='TIMEZONE_SAVE:Dawson')],
            [InlineKeyboardButton('Dawson_Creek', callback_data='TIMEZONE_SAVE:Dawson_Creek')],
            [InlineKeyboardButton('Denver', callback_data='TIMEZONE_SAVE:Denver')],
            [InlineKeyboardButton('Detroit', callback_data='TIMEZONE_SAVE:Detroit')],
            [InlineKeyboardButton('Dominica', callback_data='TIMEZONE_SAVE:Dominica')],
            [InlineKeyboardButton('Edmonton', callback_data='TIMEZONE_SAVE:Edmonton')],
            [InlineKeyboardButton('Eirunepe', callback_data='TIMEZONE_SAVE:Eirunepe')],
            [InlineKeyboardButton('El_Salvador', callback_data='TIMEZONE_SAVE:El_Salvador')],
            [InlineKeyboardButton('Ensenada', callback_data='TIMEZONE_SAVE:Ensenada')],
            [InlineKeyboardButton('Fort_Wayne', callback_data='TIMEZONE_SAVE:Fort_Wayne')],
            [InlineKeyboardButton('Fortaleza', callback_data='TIMEZONE_SAVE:Fortaleza')],
            [InlineKeyboardButton('Glace_Bay', callback_data='TIMEZONE_SAVE:Glace_Bay')],
            [InlineKeyboardButton('Godthab', callback_data='TIMEZONE_SAVE:Godthab')],
            [InlineKeyboardButton('Goose_Bay', callback_data='TIMEZONE_SAVE:Goose_Bay')],
            [InlineKeyboardButton('Grand_Turk', callback_data='TIMEZONE_SAVE:Grand_Turk')],
            [InlineKeyboardButton('Grenada', callback_data='TIMEZONE_SAVE:Grenada')],
            [InlineKeyboardButton('Guadeloupe', callback_data='TIMEZONE_SAVE:Guadeloupe')],
            [InlineKeyboardButton('Guatemala', callback_data='TIMEZONE_SAVE:Guatemala')],
            [InlineKeyboardButton('Guayaquil', callback_data='TIMEZONE_SAVE:Guayaquil')],
            [InlineKeyboardButton('Guyana', callback_data='TIMEZONE_SAVE:Guyana')],
            [InlineKeyboardButton('Halifax', callback_data='TIMEZONE_SAVE:Halifax')],
            [InlineKeyboardButton('havana', callback_data='TIMEZONE_SAVE:havana')],
            [InlineKeyboardButton('Hermosillo', callback_data='TIMEZONE_SAVE:Hermosillo')],
            [InlineKeyboardButton('Indianapolis', callback_data='TIMEZONE_SAVE:Indianapolis')],
            [InlineKeyboardButton('Inuvik', callback_data='TIMEZONE_SAVE:Inuvik')],
            [InlineKeyboardButton('Iqaluit', callback_data='TIMEZONE_SAVE:Iqaluit')],
            [InlineKeyboardButton('Jamaica', callback_data='TIMEZONE_SAVE:Jamaica')],
            [InlineKeyboardButton('Jujuy', callback_data='TIMEZONE_SAVE:Jujuy')],
            [InlineKeyboardButton('Juneau', callback_data='TIMEZONE_SAVE:Juneau')],
            [InlineKeyboardButton('Knox_IN', callback_data='TIMEZONE_SAVE:Knox_IN')],
            [InlineKeyboardButton('Kralendijk', callback_data='TIMEZONE_SAVE:Kralendijk')],
            [InlineKeyboardButton('La_Paz', callback_data='TIMEZONE_SAVE:La_Paz')],
            [InlineKeyboardButton('Lima', callback_data='TIMEZONE_SAVE:Lima')],
            [InlineKeyboardButton('Los_Angeles', callback_data='TIMEZONE_SAVE:Los_Angeles')],
            [InlineKeyboardButton('Louisville', callback_data='TIMEZONE_SAVE:Louisville')],
            [InlineKeyboardButton('Lower_Princes', callback_data='TIMEZONE_SAVE:Lower_Princes')],
            [InlineKeyboardButton('Maceio', callback_data='TIMEZONE_SAVE:Maceio')],
            [InlineKeyboardButton('Managua', callback_data='TIMEZONE_SAVE:Managua')],
            [InlineKeyboardButton('Manaus', callback_data='TIMEZONE_SAVE:Manaus')],
            [InlineKeyboardButton('Marigot', callback_data='TIMEZONE_SAVE:Marigot')],
            [InlineKeyboardButton('Martinique', callback_data='TIMEZONE_SAVE:Martinique')],
            [InlineKeyboardButton('Matamoros', callback_data='TIMEZONE_SAVE:Matamoros')],
            [InlineKeyboardButton('Mazatlan', callback_data='TIMEZONE_SAVE:Mazatlan')],
            [InlineKeyboardButton('Mendoza', callback_data='TIMEZONE_SAVE:Mendoza')],
            [InlineKeyboardButton('Menominee', callback_data='TIMEZONE_SAVE:Menominee')],
            [InlineKeyboardButton('Merida', callback_data='TIMEZONE_SAVE:Merida')],
            [InlineKeyboardButton('Metlakatla', callback_data='TIMEZONE_SAVE:Metlakatla')],
            [InlineKeyboardButton('Mexico_City', callback_data='TIMEZONE_SAVE:Mexico_City')],
            [InlineKeyboardButton('Miquelon', callback_data='TIMEZONE_SAVE:Miquelon')],
            [InlineKeyboardButton('Moncton', callback_data='TIMEZONE_SAVE:Moncton')],
            [InlineKeyboardButton('Monterrey', callback_data='TIMEZONE_SAVE:Monterrey')],
            [InlineKeyboardButton('Montevideo', callback_data='TIMEZONE_SAVE:Montevideo')],
            [InlineKeyboardButton('Montreal', callback_data='TIMEZONE_SAVE:Montreal')],
            [InlineKeyboardButton('Montserrat', callback_data='TIMEZONE_SAVE:Montserrat')],
            [InlineKeyboardButton('Nassau', callback_data='TIMEZONE_SAVE:Nassau')],
            [InlineKeyboardButton('New_York', callback_data='TIMEZONE_SAVE:New_York')],
            [InlineKeyboardButton('Nipigon', callback_data='TIMEZONE_SAVE:Nipigon')],
            [InlineKeyboardButton('Nome', callback_data='TIMEZONE_SAVE:Nome')],
            [InlineKeyboardButton('Noronha', callback_data='TIMEZONE_SAVE:Noronha')],
            [InlineKeyboardButton('Ojinaga', callback_data='TIMEZONE_SAVE:Ojinaga')],
            [InlineKeyboardButton('Panama', callback_data='TIMEZONE_SAVE:Panama')],
            [InlineKeyboardButton('Pangnirtung', callback_data='TIMEZONE_SAVE:Pangnirtung')],
            [InlineKeyboardButton('Paramaribo', callback_data='TIMEZONE_SAVE:Paramaribo')],
            [InlineKeyboardButton('Phoenix', callback_data='TIMEZONE_SAVE:Phoenix')],
            [InlineKeyboardButton('Port-au-Prince', callback_data='TIMEZONE_SAVE:Port-au-Prince')],
            [InlineKeyboardButton('Port_of_Spain', callback_data='TIMEZONE_SAVE:Port_of_Spain')],
            [InlineKeyboardButton('Porto_Acre', callback_data='TIMEZONE_SAVE:Porto_Acre')],
            [InlineKeyboardButton('Porto_Velho', callback_data='TIMEZONE_SAVE:Porto_Velho')],
            [InlineKeyboardButton('Puerto_Rico', callback_data='TIMEZONE_SAVE:Puerto_Rico')],
            [InlineKeyboardButton('Rainy_River', callback_data='TIMEZONE_SAVE:Rainy_River')],
            [InlineKeyboardButton('Rankin_Inlet', callback_data='TIMEZONE_SAVE:Rankin_Inlet')],
            [InlineKeyboardButton('Recife', callback_data='TIMEZONE_SAVE:Recife')],
            [InlineKeyboardButton('Regina', callback_data='TIMEZONE_SAVE:Regina')],
            [InlineKeyboardButton('Resolute', callback_data='TIMEZONE_SAVE:Resolute')],
            [InlineKeyboardButton('Rio_Branco', callback_data='TIMEZONE_SAVE:Rio_Branco')],
            [InlineKeyboardButton('Rosario', callback_data='TIMEZONE_SAVE:Rosario')],
            [InlineKeyboardButton('Santa_Isabel', callback_data='TIMEZONE_SAVE:Santa_Isabel')],
            [InlineKeyboardButton('Santarem', callback_data='TIMEZONE_SAVE:Santarem')],
            [InlineKeyboardButton('Santiago', callback_data='TIMEZONE_SAVE:Santiago')],
            [InlineKeyboardButton('Santo_Domingo', callback_data='TIMEZONE_SAVE:Santo_Domingo')],
            [InlineKeyboardButton('Sao_Paulo', callback_data='TIMEZONE_SAVE:Sao_Paulo')],
            [InlineKeyboardButton('Scoresbysund', callback_data='TIMEZONE_SAVE:Scoresbysund')],
            [InlineKeyboardButton('Shiprock', callback_data='TIMEZONE_SAVE:Shiprock')],
            [InlineKeyboardButton('Sitka', callback_data='TIMEZONE_SAVE:Sitka')],
            [InlineKeyboardButton('St_Barthelemy', callback_data='TIMEZONE_SAVE:St_Barthelemy')],
            [InlineKeyboardButton('St_Johns', callback_data='TIMEZONE_SAVE:St_Johns')],
            [InlineKeyboardButton('St_Kitts', callback_data='TIMEZONE_SAVE:St_Kitts')],
            [InlineKeyboardButton('St_Lucia', callback_data='TIMEZONE_SAVE:St_Lucia')],
            [InlineKeyboardButton('St_Thomas', callback_data='TIMEZONE_SAVE:St_Thomas')],
            [InlineKeyboardButton('St_Vincent', callback_data='TIMEZONE_SAVE:St_Vincent')],
            [InlineKeyboardButton('Swift_Current', callback_data='TIMEZONE_SAVE:Swift_Current')],
            [InlineKeyboardButton('Tegucigalpa', callback_data='TIMEZONE_SAVE:Tegucigalpa')],
            [InlineKeyboardButton('Thule', callback_data='TIMEZONE_SAVE:Thule')],
            [InlineKeyboardButton('Thunder_Bay', callback_data='TIMEZONE_SAVE:Thunder_Bay')],
            [InlineKeyboardButton('Tijuana', callback_data='TIMEZONE_SAVE:Tijuana')],
            [InlineKeyboardButton('Toronto', callback_data='TIMEZONE_SAVE:Toronto')],
            [InlineKeyboardButton('Tortola', callback_data='TIMEZONE_SAVE:Tortola')],
            [InlineKeyboardButton('Vancouver', callback_data='TIMEZONE_SAVE:Vancouver')],
            [InlineKeyboardButton('Virgin', callback_data='TIMEZONE_SAVE:Virgin')],
            [InlineKeyboardButton('Whitehorse', callback_data='TIMEZONE_SAVE:Whitehorse')],
            [InlineKeyboardButton('Winnipeg', callback_data='TIMEZONE_SAVE:Winnipeg')],
            [InlineKeyboardButton('Yakutat', callback_data='TIMEZONE_SAVE:Yakutat')],
            [InlineKeyboardButton('Yellowknife', callback_data='TIMEZONE_SAVE:Yellowknife')],
        ]

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


updater = Updater('189612249:AAFRvgiS71TiU6mb6Pu_nf0gVHmNMdc-8h0')

updater.dispatcher.add_handler(CommandHandler('info', start))
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('teammarilu', teammarilu))
updater.dispatcher.add_handler(CommandHandler('drive', drive))
updater.dispatcher.add_handler(CommandHandler('checkpoints', checkpoints))
updater.dispatcher.add_handler(CommandHandler('settings', settings_menu))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

#jobqueue = updater.job_queue
#checkpoint_queue = Job(notify_checkpoint, 10.0)
#jobqueue.put(checkpoint_queue, next_t=5.0)

updater.start_polling()
updater.idle()
