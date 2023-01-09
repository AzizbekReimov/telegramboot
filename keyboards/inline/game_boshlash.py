from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


game_boshlash = CallbackData("game_boshlash", "item_name")

gameMenu = InlineKeyboardMarkup(row_width=2)

boshlaymizmi = InlineKeyboardButton(text="Boshlash", callback_data=game_boshlash.new(item_name="boshlash"))
toxtatish = InlineKeyboardButton(text="To'xtatish", callback_data=game_boshlash.new(item_name="toxtatish"))

gameMenu.insert(boshlaymizmi)
gameMenu.insert(toxtatish)
