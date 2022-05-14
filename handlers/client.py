import os
import time

from aiogram import types, Dispatcher
from main import collect_data
from keyboard import kb_client
from bot_config import bot


async def start_hi(message: types.message):
    await message.reply(f'Привет!', reply_markup=kb_client)


async def scrapper(message: types.message):
    await message.reply("Start scrapping... ")
    for i in range(1, 9):
        time.sleep(3)
        file = await collect_data(i).__anext__()
        with open(f"{file}", 'r') as f:
            text = f.read()
            os.remove(file)
        await bot.send_message(message.from_user.id, text, disable_web_page_preview=True)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_hi,
                                lambda message: message.text.lower().strip() in ['start', '/start'])
    dp.register_message_handler(scrapper, lambda message: message.text.lower().strip() in ['scrapper', '/scrapper'])
