# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 00:16:53 2022

@author: BotirDev
"""

import logging
import wikipedia
 
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5037610079:AAGWZJWxiKlsbSC1dVtgthZI2LHIv3LP8E8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Select language
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   """
   This handler will be called when user sends `/start` or `/help` command
   """
   await message.reply("Assalom alaykum Izla Va Top botiga xush kelibsiz")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
        
    except:
        await message.answer("Bu mavzudagi maqola topilmadi !")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)