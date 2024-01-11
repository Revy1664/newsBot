import telebot

from config import API_KEY, URL
from parser import get_data

# initializing bot
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
	"""
		send welcome to user
	"""

	bot.send_message(message.chat.id, "Хэй! Что нового?😉")

@bot.message_handler(content_types="text")
def send_news(message):
	"""
		send news to user
	"""
	if message.text == "Новости":
		news = ""
		data = get_data(URL)

		# message generation
		for (header, url) in data.items():
			news += f"{header}\n{url}\n\n"

		bot.send_message(message.chat.id, news)

bot.infinity_polling()