import telebot

bot = telebot.TeleBot("975958816:AAGLi7yZgMErf3EwgaapEwSkBgufKurlQnk")

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):

	if message.text == 'Hello':
		bot.send_message(message.from_user.id, 'Hey, how are you? I`m Aragorn - new chatbot')
	elif message.text == '/start':
		bot.send_message(message.from_user.id, 'Let`s hit the chat!')
	else:
		bot.send_message(message.from_user.id, 'Sorry, didn`t get you, could you repeat ?')

bot.polling(none_stop=True, interval=0)