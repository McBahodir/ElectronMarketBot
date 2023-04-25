from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config import BOT_TOKEN
from handlers.user import register_user_py

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher: Dispatcher):
    register_user_py(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
