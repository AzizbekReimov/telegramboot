from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from datetime import datetime as dt
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    text = f"Ассалому алейкум <b>{msg.from_user.full_name}</b>\n\n"
    text += f"<b>Бот хакида кискача малумот:</b>\n"
    text += f"Ушбу ботда сиз достларингиз билан сервер очиб содда ойин ойнашингиз мумкин🎮\n\n"
    text += f"<b>камандалар:</b>\n"
    text += f"Сервер яратиш учун /creat_server камандасини босинг.\n"
    text += f"Ёки брорта серверда ойнамокчи булсангиз /get_server камандасини босинг.\n\n   "
    text += f"<b>Мурожат учун:</b>\n"
    text += f"Таклф Ёки саволлар булса куйидаги админ блан богдланинг @azizbek_reimov\n"
    await msg.answer(f"{text}")
