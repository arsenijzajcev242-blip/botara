from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Каталог', callback_data='catalog'),InlineKeyboardButton(text='Корзина',callback_data='seat')],
                                      [InlineKeyboardButton(text='Профиль',callback_data='profile')]])
