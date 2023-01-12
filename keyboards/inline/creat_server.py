from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

server_callback = CallbackData("create_post", "action")

server_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Serverni Yaratish", callback_data=server_callback.new(action="creat")),
        InlineKeyboardButton(text="❌ Rad etish", callback_data=server_callback.new(action="cancel")),
    ]]
)
