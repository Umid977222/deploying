from aiogram import executor
from bot.control import dp


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)