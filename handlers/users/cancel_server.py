from aiogram import types

from loader import dp, bot
from data.config import servers, server_keys
import time

@dp.message_handler(commands="cancel_server")
async def cancel_server(msg: types.Message):
    royxat = {}
    for server in server_keys:
        royxat[server]=servers[server]['players']
    son = 0
    text = ""
    text1 = ""
    for key, value in royxat.items():
        if msg.from_user.id not in royxat[key]:
            text += f"Сиз ({key}) сервер ройхатида йоксиз❌\n"
        elif msg.from_user.id in royxat[key]:
            royxat[key].remove(msg.from_user.id)
            text1 += f"<b>Сиз ({key}) сервер ройхатидан чикдингиз</b>✅\n"
            await msg.answer("🔍")
            time.sleep(3.7)
            await msg.answer(text=f"{text}{text1}")
            break
