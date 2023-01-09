from aiogram import types

from loader import dp, bot

from keyboard.inline.game_boshlash import gameMenu

id_royxati = []

@dp.message_hendler(commands="game")
async def bot_start(message: types.Message):
	text = (f"<b>O'yini Boshlaysizmi?</b>\n\n",
				 f"<b>Boshlash uchun</b>: <u>\"Boshlash\"</u> Tugmasini bosing\n",
				 f"<b>O'ynashni xoxlamasangiz</b>: <u>To'xtatish</u> Tugmasini bosing\n",
				 f"<b>O'yin qachon boshlanadi</b>: qachonki o'yinga 10ta odam yigiladi oshandan song boshlanadi")
	await message.answer(text, reply_markup=gameMenu)

@dp.message_handler()
async def bot_start(message: types.Message):
	if len(id_royxati)<10:
		if message.from_user.id not in id_royxati:
			id_royxati.append(message.from_user.id)
			id_royxat = id_royxati[:]
			id_royxat.remove(message.from_user.id)
			for id in id_royxat:
				await bot.send_message(chat_id=id, text=f"Ойинга 1та одам кошилди.\n <b>Жами Ойнчи сони</b>: {len(id_royxati)} ta")
			await message.answer(f"siz oynga qoshildingiz")
		else:
			await message.answer("siz oyinga qoshilgansiz")