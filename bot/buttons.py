from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Mahsulotni qidirish: 🔎'), ]
    ]
)
