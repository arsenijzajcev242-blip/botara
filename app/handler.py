from aiogram import types, Router,F
from aiogram.filters import CommandStart
import app.keyboard as kb
router = Router()
@router.message(CommandStart())
async def hello_world(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!",reply_markup=kb.main)
@router.callback_query(F.data == 'catalog')
async def catalog(callback_query: types.CallbackQuery):
    await callback_query.answer('Вы выбрали каталог')
    await callback_query.message.edit_text('Вы находитесь в каталоге')
@router.callback_query(F.data == 'seat')
async def seat(callback_query: types.CallbackQuery):
    await callback_query.answer('Вы выбрали корзину')
    await callback_query.message.edit_text('Вы в корзине')
@router.callback_query(F.data == 'profile')
async def profile(callback_query: types.CallbackQuery):
    await callback_query.answer('Вы выбрали профиль')
    await callback_query.message.edit_text('Вы в профиле')

