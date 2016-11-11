from telegram.ext import Updater, CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from pydrive.auth import GoogleAuth
import sqlite3 as lite
from time import mktime
from datetime import datetime, timedelta
from unicodedata import normalize

def start(bot, update):
    update.message.reply_text('Oli')

def hello(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))

def teammarilu(bot, update):
    update.message.reply_text('Invocando a @Rottenman @victorono @MalKarakter')

def drive(bot, update):
    gauth = GoogleAuth()
    auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
    code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
    gauth.Auth(code) # Authorize and build service from the code

def get_gmt(p_chat_id, p_chat_title, p_chat_username):
    update.message.reply_text('get_gmt...')
    conn = lite.connect('gmt.db')
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
    update.message.reply_text('checkpoints...1')
    update.message.reply_text(format(update.message.chat))
    chatid = update.message.chat.id
    chattitle = update.message.chat.title
    chatusername = update.message.chat.username
    gmt_value = get_gmt(chatid, chattitle, chatusername)
    update.message.reply_text('checkpoints...2')
    t0 = datetime.strptime('2014-07-09 15', '%Y-%m-%d %H') + timedelta(hours=gmt_value)
    update.message.reply_text('checkpoints...3')
    hours_per_cycle = 175

    update.message.reply_text('checkpoints...4')

    t = datetime.now()

    update.message.reply_text('checkpoints...5')

    seconds = mktime(t.timetuple()) - mktime(t0.timetuple())
    update.message.reply_text('checkpoints...6')
    cycles = seconds // (3600 * hours_per_cycle)
    update.message.reply_text('checkpoints...7')
    start = t0 + timedelta(hours=cycles * hours_per_cycle)
    update.message.reply_text('checkpoints...8')
    checkpoints = map(lambda x: start + timedelta(hours=x), range(0, hours_per_cycle, 5))
    update.message.reply_text('checkpoints...9')
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

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        # remove update.message.chat_id from conversation list
        update.message.reply_text('Unauthorized')
    except BadRequest:
        # handle malformed requests - read more below!
        update.message.reply_text('BadRequest')
    except TimedOut:
        # handle slow connection problems
        update.message.reply_text('TimedOut')
    except NetworkError:
        # handle other connection problems
        update.message.reply_text('NetworkError')
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        update.message.reply_text('ChatMigrated')
    except TelegramError:
        # handle all other telegram related errors
        update.message.reply_text('TelegramError')

updater = Updater('189612249:AAFRvgiS71TiU6mb6Pu_nf0gVHmNMdc-8h0')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('teammarilu', teammarilu))
updater.dispatcher.add_handler(CommandHandler('drive', drive))
updater.dispatcher.add_handler(CommandHandler('checkpoints', checkpoints))
updater.dispatcher.add_error_handler(error_callback)

updater.start_polling()
updater.idle()
