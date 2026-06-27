from aiogram import types, Router
from aiogram.filters import CommandStart

router = Router()
@router.message(CommandStart())
async def hello_world(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")

