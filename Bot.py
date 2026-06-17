import telebot
import os
from deep_translator import GoogleTranslator

# Replace 'YOUR_TOKEN_HERE' with your actual bot token, 
# or use an environment variable as shown below
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        # Translates text to English
        translated = GoogleTranslator(source='auto', target='en').translate(message.text)
        bot.reply_to(message, f"Translated: {translated}")
    except Exception as e:
        bot.reply_to(message, "Sorry, I couldn't translate that.")

print("Bot is running...")
bot.polling()

