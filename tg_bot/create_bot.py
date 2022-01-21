import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .settings import TOKEN


storage = MemoryStorage()

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
bot_name = loop.run_until_complete(bot.get_me())['username']
