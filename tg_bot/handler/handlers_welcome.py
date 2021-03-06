import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.utils.markdown import hspoiler

from create_bot import dp


@dp.message_handler(commands=["start"])
async def start_messages(message: types.Message, state: FSMContext):
    """Handle /spoiler command and answer with spoiler."""

    connect = await aiohttp.ClientSession(trust_env=True).get(
        'http://web:8000/api/v1/client/',
        ssl=False,
    )
    request = await connect.json()
    list_user = []
    for user in request:
        list_user.append(user['email'])
    text = '\n'.join(list_user)
    await message.answer(
        f"Spoiler: {hspoiler(f'{text}')}",
        parse_mode=ParseMode.HTML)


