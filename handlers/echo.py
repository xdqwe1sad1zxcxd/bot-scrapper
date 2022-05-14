from aiogram import types, Dispatcher


async def echo(message: types.message):
    await message.delete()


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
