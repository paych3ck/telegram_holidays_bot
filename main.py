import telebot
import holidays_func

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row("Праздники сегодня")
    bot.send_message(message.chat.id, "Бот запущен!", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def call(message):
    if message.text == "Праздники сегодня":
        bot.send_message(message.chat.id, holidays_func.show_holidays())


if __name__ == "__main__":
    bot.infinity_polling()
