from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Oli')

def hello(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))

def teammarilu(bot, update):
    update.message.reply_text('Invocando a @Rottenman @victorono @MalKarakter')

updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('teammarilu', teammarilu))

updater.start_polling()
updater.idle()
