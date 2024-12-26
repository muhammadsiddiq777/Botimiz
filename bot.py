import telebot
from googletrans import Translator

# Bot tokenini kiriting
BOT_TOKEN = "8169173541:AAHbLXbACHd5hfY9UH0raRaBcJ3-RITsYOA"

# Bot yaratish
bot = telebot.TeleBot(BOT_TOKEN)

# Tarjima funksiyasi uchun translator obyekti
translator = Translator()

# /start yoki /help komandalariga javob
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Salom! Men tarjima botman.\n"
        "Matnni yuboring, va men uni ingliz tilidan o'zbek tiliga (yoki aksincha) tarjima qilaman."
    )

# Tarjima qiluvchi asosiy handler
@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        # Matnni tarjima qilish
        translation = translator.translate(message.text, src='auto', dest='uz')
        bot.reply_to(message, f"Tarjima:\n{translation.text}")
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, tarjima qilishda xatolik yuz berdi.")

# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling()
