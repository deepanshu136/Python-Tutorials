import logging
from telegram.ext import *
import responses



API_KEY='5262610202:AAFcLZCUifLPqqvsWaUZk6S9kraNrqiSTb0'

# set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s  %(message)s', level=logging.INFO)
logging.info('starting Bot..')

def start_command(update,context):
    update.message.reply_text('hello there! I\'am  pheonix. What\'s up? ')


def help_command(update,context):
    update.message.reply_text(' Can ask your query? I will try to respond it. ')


def custom_command(update,context):
    update.message.reply_text('It was nic to talk to you. ')


def hendle_message(update,context):
         text=str(update.message.text).lower()