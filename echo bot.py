# Автор: Василь Онуфрійчук
# Ехо бот для телеграма.
# https://github.com/8a7l/py_ebtg
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


updater = Updater(token='Місце для токена.', use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
dispatcher = updater.dispatcher

def com(a,b):
    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text=b)
    start_handler = CommandHandler(a, start)
    dispatcher.add_handler(start_handler)
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вибачте, я не розумію цю команду.")
def update():
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    updater.start_polling()
def main():
    mesagges()
    update()
def mesagges():
    #===================================================================
    com('start','Команда /start показує цей текст.')
    com('help','Команда /help показує цей текст.')
    #===================================================================

if __name__=='__main__':
    main()
