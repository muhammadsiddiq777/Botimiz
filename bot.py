from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from googletrans import Translator

# Bot tokenini kiriting
BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"

# Bot va dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Tarjima funksiyasi uchun translator obyekti
translator = Translator()

# /start yoki /help komandalariga javob
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Salom! Men tarjima botman.\n"
        "Matnni yuboring, va men uni ingliz tilidan o'zbek tiliga (yoki aksincha) tarjima qilaman."
    )

# Tarjima qiluvchi asosiy handler
@dp.message_handler()
async def translate_text(message: types.Message):
    try:
        # Matnni tarjima qilish
        translation = translator.translate(message.text, src='auto', dest='uz')
        await message.reply(f"Tarjima:\n{translation.text}")
    except Exception as e:
        await message.reply("Kechirasiz, tarjima qilishda xatolik yuz berdi.")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)