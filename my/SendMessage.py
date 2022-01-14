import telegram

token = "5049892347:AAGQuOsErngVjhRixKO3Z8lrVwfi3ypiwX4"
bot = telegram.Bot(token)
bot.send_message(chat_id=5018530970, text="Hello world!")
bot.send_message(chat_id=5018530970, text="Hello, bot")