from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot

id_royxati = [1, 2, 3, 4, 5, 6, 7, 8]
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
	await message.answer(f"Salom {message.from_user.full_name}!")
	if len(id_royxati)<10:
		await message.answer("oyin boshlanib bolgan")
		if message.from_user.id not in id_royxati:
			id_royxati.append(message.from_user.id)
			#for id_royxat in id_royxati:
				#await bot.send_message(chat_id=id_royxat, text=f"oyinga 1ta odam qo'shild")
	await message.answer("oyin boshlanib bolgan")
