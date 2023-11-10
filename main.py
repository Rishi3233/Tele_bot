import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Welcome to Talking Bot.")

def helps(update, context):
    update.message.reply_text(
        """
        Hi there! I'm Telegram bot Created by Kushh. Please follow these commands:-

        /start - to start the conversation 
        /content - Information about Talking bot
        /contact - Information about contact of kushh
        /help - to get this help menu

        I hope this helps :)
        """
    )


def content(update, context):
    update.message.reply_text(
        """
        This is bot which give the your info to our leader who try not to solve the 
        problem but fix it after working on it. It will respond within a hour. so, please 
        trust our leader and wait for a while 😃....
        """
    )


def contact(update, context):
    update.message.reply_text(
        """
        If u have a query so please free to ask on the give details below:))
        .........
        .........

        """  
    )

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")



updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('content', content))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()

