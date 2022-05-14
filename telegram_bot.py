from aiogram import executor
from bot_config import bot, dp
from handlers import client, echo


client.register_handlers_client(dp)
echo.register_handlers_echo(dp)


async def on_startup(_):
    print('[+] Бот запущен!')
    await bot.send_message(5167573237, '[+] Бот запущен!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
