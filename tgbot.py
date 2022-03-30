import telebot
import qrcode
import time

token = ""
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m, res=False):
	bot.send_message(m.chat.id, "отправь мне любой текст. не более 1000 символов.")


def qrgen(text):
	qrcode_img = qrcode.make(text)
	type(qrcode_img)
	qrcode_img.save("qrcode.png")


@bot.message_handler(content_types=["text", "photo"])
def handle_text(message):
	if len(message.text) < 1000:
		qrgen(message.text)
		qrcode_img = open('qrcode.png', 'rb')
		bot.send_photo(message.chat.id, qrcode_img)


bot.polling(non_stop=True, interval=0)
