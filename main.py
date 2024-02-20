from googletrans import Translator
from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot import types
bot = AsyncTeleBot("6421378542:AAFfOwCqzYfEqCAiL5F6dtl18QMgiS8Lza0", parse_mode=None)
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, '------\n'
                       + 'Здравствуй, '
                       + message.from_user.first_name
                       + ' \nПереведу с русского на английский \nИ с других языков на русский '
                       + '\n------')
@bot.message_handler(commands=['help'])
async def send_welcome(message):
    await bot.reply_to(message, '------\n'
                       + 'Просто вводи текст и нажимай отправить\n'
                       + 'Я сам определю какой это язык\n'
                       + 'Если не перевел, попробуй еще раз\n'
                       + 'Перевод google'
                       + '\n------')
@bot.message_handler()
async def user_text(message):
    translator = Translator()
    lang = translator.detect(message.text)
    lang = lang.lang
    if lang == 'ru':
        send = translator.translate(message.text)
        await bot.reply_to(message, '------\n' + send.text + '\n------')
    else:
        send = translator.translate(message.text, dest='ru')
        await bot.reply_to(message, '------\n' + send.text + '\n------')
asyncio.run(bot.infinity_polling())