# -*- coding: utf-8 -*-

import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define the function to handle the /start command
def start(update, context):
    # Get the username of the user who called the bot
    username = update.effective_user.username

    # Generate a random number between 1 and 101
    number = random.randint(1, 101)
    # Create the message to send
    message = f"@{username} сьогодні криса на {number} %. \U0001F60E \U0001F400"
    # Create the button to call the bot again
    callback_data = f"{username}:{number}"
    button = InlineKeyboardButton("Я сьогодні криса на ...", callback_data=callback_data)
    keyboard = InlineKeyboardMarkup([[button]])
    # Send the message to the user with the button
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=keyboard)

# Define the function to handle the button callback
def button_callback(update, context):
    query = update.callback_query
    # Get the username and number from the callback data
    username = update.effective_user.username
    # Generate a new number between 1 and 101
    number = random.randint(1, 101)
    # Create the message to send

    message = f"@{username} сьогодні криса на {number} %. \U0001F60E \U0001F400"
    # Create the button to call the bot again
    callback_data = f"{username}:{number}"
    button = InlineKeyboardButton("Я сьогодні криса на ...", callback_data=callback_data)

    keyboard = InlineKeyboardMarkup([[button]])
    # Send the new message to the user with the new button
    context.bot.send_message(chat_id=query.message.chat_id, text=message, reply_markup=keyboard)

# Set up the Telegram bot
bot_token = ''
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Add the /start command handler
start_handler = CommandHandler('rat', start)
dispatcher.add_handler(start_handler)

# Add the button callback handler
button_handler = CallbackQueryHandler(button_callback)
dispatcher.add_handler(button_handler)

# Start the bot
updater.start_polling()
