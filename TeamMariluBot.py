from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Job, CallbackQueryHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from pydrive.auth import GoogleAuth
import sqlite3 as lite
from time import mktime
from datetime import datetime, timedelta
from unicodedata import normalize

def settings(bot, update):
    keyboard =  [
                    [InlineKeyboardButton("Africa", callback_data='Africa'), InlineKeyboardButton("America", callback_data='America'), InlineKeyboardButton("Asia", callback_data='Asia'), InlineKeyboardButton("Australia", callback_data='Australia')],
                    [InlineKeyboardButton("Europe", callback_data='Europe'), InlineKeyboardButton("Indian", callback_data='Indian'), InlineKeyboardButton("Pacific", callback_data='Pacific')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Configurando zona horaria:', reply_markup=reply_markup)


def timezone_africa(bot, update):
    print '--timezone_africa--'

def button(bot, update):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id

    if data == 'Africa':
        print 'Africa...'
        #timezone_africa()

    elif data == 'America':
        print 'America...'

    elif data == 'Asia':
        print 'Asia...'

    elif data == 'Australia':
        print 'Australia...'

    elif data == 'Europe':
        print 'Europa...'

    elif data == 'Indian':
        print 'India...'

    elif data == 'Pacific':
        print 'Pacifico...'

    else:
        print 'timezone...'

    bot.editMessageText(text="Zona horaria: %s" % query.data, chat_id=query.message.chat_id, message_id=query.message.message_id)


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
    bot.sendMessage('Invocan a @Rottenman @victorono @MalKarakter')


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
updater.dispatcher.add_handler(CommandHandler('settings', settings))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

#jobqueue = updater.job_queue
#checkpoint_queue = Job(notify_checkpoint, 10.0)
#jobqueue.put(checkpoint_queue, next_t=5.0)

updater.start_polling()
updater.idle()
