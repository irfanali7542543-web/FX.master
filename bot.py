import os
import telebot

TOKEN = "8855486058:AAFi7i88y0mLjXjPGmlodYaGr8uf2vmk8j4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Main Irfan_bot hoon, mera kaam shuru ho gaya hai!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Aapne kaha: {message.text}")

if __name__ == '__main__':
    print("Bot polling shuru ho gayi hai...")
    bot.infinity_polling()
