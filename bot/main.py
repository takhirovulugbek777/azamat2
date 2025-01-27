import asyncio
import logging
import sys
import requests
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from buttons import button
from api import create_user
from api import BASE_URL

TOKEN = "7192339698:AAFLPA9gcKIpAqM2JYzf0Y3rMtlDzrwPdnU"

dp = Dispatcher()


# Start komandasi uchun handler
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    result = create_user(message.from_user.id, message.from_user.first_name, message.from_user.username)
    await message.answer(
        f"Assalomu alaykum, {html.bold(message.from_user.full_name)}!\n"
        f"{result}\n"
        f"Telefon yoki MacBook seriya raqamini kiriting:"
    )


# Ma'lumotlarni olish uchun handler
@dp.message()
async def message_handler(message: Message) -> None:
    serial_number = message.text.strip()
    try:
        response = requests.get(BASE_URL + f'products/{serial_number}')
        if response.status_code == 200:
            a = response.json()
            reply_text = (
                f"🔍 Mahsulot ma'lumotlari:\n"
                f"📦 Nomi: {a.get('name', 'Noma\'lum')}\n"
                f"📅 Sotilgan sana: {a.get('sold_date', 'Noma\'lum')}\n"
                f"📜 Serial raqam: {a.get('serial_number', 'Noma\'lum')}\n"
                f"✅ Kafolat holati: {'Aktiv' if a.get('is_warranty_active') else 'Muddati o\'tgan'}\n"
                f"📆 Kafolat muddati: {a.get('warranty_period', 'Noma\'lum')} oy\n"
            )
            await message.answer(reply_text)
        elif response.status_code == 404:
            await message.answer("❌ Mahsulot topilmadi. Iltimos, serial raqamini tekshiring.")
        else:
            await message.answer("❌ Xatolik yuz berdi. Keyinroq qayta urinib ko'ring.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Xatolik: {e}")
        await message.answer("❌ Server bilan bog'lanishda xatolik yuz berdi. Keyinroq urinib ko'ring.")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
