import telebot
import os

TOKEN = "8863970147:AAGbOhwj0HM_SZvllRFjKW5qDng0lf1GdPE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👑 البوت يعمل الآن من السيرفر!")

bot.infinity_polling()
