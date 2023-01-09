from aiogram import types

from loader import dp, bot

from keyboards.inline.game_boshlash import gameMenu, game_boshlash

id_royxati = []

@dp.message_handler(commands="game")
async def bot_start(message: types.Message):
	text = (f"<b>O'yini Boshlaysizmi?</b>",
				 f"<b>Boshlash uchun</b>: <u>Boshlash</u> Tugmasini bosing",
				 f"<b>O'ynashni xoxlamasangiz</b>: <u>To'xtatish</u> Tugmasini bosing\n",
				 f"<b>Savol?</b>\n"
				 f"<b>O'yin qachon boshlanadi</b>: qachonki o'yinga 10ta odam yigiladi oshandan song boshlanadi")
	await message.answer("\n".join(text), reply_markup=gameMenu)

@dp.callback_query_handler(game_boshlash.filter(item_name="boshlash"))
async def bot_start(call: types.CallbackQuery):
	if len(id_royxati)<10:
		if call.from_user.id not in id_royxati:
			id_royxati.append(call.from_user.id)
			id_royxat = id_royxati[:]
			id_royxat.remove(call.from_user.id)
			for id in id_royxat:
				await bot.send_message(chat_id=id, text=f"Ойинга 1та одам кошилди.\n <b>Жами Ойнчи сони</b>: {len(id_royxati)} ta")
			await bot.send_message(chat_id=call.from_user.id, text=f"siz oynga qoshildingiz")
		else:
			await bot.send_message(chat_id=call.from_user.id, text=f"siz oyinga qoshilgansiz")	
	await call.answer(cache_time=60)
	await call.message.edit_reply_markup()

@dp.callback_query_handler(game_boshlash.filter(item_name="toxtatish"))
async def bot_start(call: types.CallbackQuery):
	if call.from_user.id not in id_royxati:
		await bot.send_message(chat_id=call.from_user.id, text=f"O'yin bekor qilindi")
	else:
		await bot.send_message(chat_id=call.from_user.id, text=f"Siz o'yinga qoshilib bolgansiz!. \n O'yindan chiqishni xoxlasangiz /cancel commandasini bosing")
	await call.answer(cache_time=60)
	await call.message.edit_reply_markup()
