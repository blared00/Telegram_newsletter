import logging

from aiogram import Dispatcher
from aiogram.types import BotCommand
from aiogram.utils import executor
from create_bot import dp
import handler

"""Логирование"""
logging.basicConfig(level=logging.DEBUG)


async def set_commands(dispatcher: Dispatcher):
    """Функция регистрации команд бота, при его запуске.
    ______
    :param dispatcher.
    """
    await dispatcher.bot.set_my_commands([
        BotCommand(command="/start", description="Для запуска бота воспользуйтесь порталом"),
    ])


# @dp.async_task
# async def scheduler():
#     """Запуск вопросов каждый день в TIME_START_POLL чата id = chat_id"""
#     aioschedule.every().day.at("9:40").do(send_question_all_users)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(60)


async def on_startup(dispatcher: Dispatcher):
    """Функция регистрации  хэндлеров бота, при его запуске.
    ______
    :param dispatcher.
    """
    await set_commands(dispatcher)
    # await scheduler()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, )#on_startup=on_startup
