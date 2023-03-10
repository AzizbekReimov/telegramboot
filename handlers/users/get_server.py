from aiogram import types
from typing import Union
from loader import dp, bot

from data.config import servers, server_keys
from keyboards.inline.get_servers import Servers, Server, menu_cd, add_serverr
from .creat_server import server_menu
import time

servername = []
@dp.message_handler(commands="get_server")
async def show_menu(message: types.Message):
    await list_categories(message)

add_server_xaqida = []
async def list_categories(messagee: Union[types.CallbackQuery, types.Message], **kwargs):
    markup = await Servers()
    royxat = []
    for serverrr in server_keys:
        players = servers[serverrr]['players']
        for player in players:
            royxat.append(player)
    if messagee.from_user.id not in royxat:
        if isinstance(messagee, types.Message):
            await messagee.answer(f"<b>~~~~~~~~~~~~~~~~~~~~~~~~~~</b>\n<b>Серверлар ройхати</b>\n<b>Мавжуд серверлар сони:</b> {len(servers)}\n\
    <b>~~~~~~~~~~~~~~~~~~~~~~~~~~</b>", reply_markup=markup)
            
        elif isinstance(messagee, types.CallbackQuery):
            call = messagee
            await call.message.edit_text(text=f"<b>~~~~~~~~~~~~~~~~~~~~~~~~~~</b>\n<b>Серверлар ройхати</b>\n<b>Мавжуд серверлар сони</b> {len(servers)}\n\
    <b>~~~~~~~~~~~~~~~~~~~~~~~~~~</b>", reply_markup=markup)
    else:
        await add_server(messagee=messagee)
    
async def show_item(callback: types.CallbackQuery, item_id):
    markup = Server(item_id)

    server_malumoti = servers[item_id]
    add_server_xaqida.append(server_malumoti)
    text = server_malumoti['players']
    await callback.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(menu_cd.filter(item_id="add_server"))
async def add_server(messagee: Union[types.CallbackQuery, types.Message]):
    try:
        players = add_server_xaqida[-1]['players']
    except IndexError:
        call = messagee
        await call.answer(f"Siz oldindan serverga ulangansiz serverdan chiqish uchun /cancel_server commandasiga murojat qiling")
    else:
        if isinstance(messagee, types.CallbackQuery):
            players.append(messagee.from_user.id)
            await messagee.message.edit_text(text=f"Siz serverga qoshildingiz")
        elif messagee:
            await messagee.answer(f"Siz oldindan serverga ulangansiz serverdan chiqish uchun /cancel_server commandasiga murojat qiling")
            del add_server_xaqida[-1]
            

@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):

    current_level = callback_data.get("level")

    item_id = callback_data.get("item_id")

    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": show_item,  # Mahsulotni ko'rsatamiz
    }
    current_level_function = levels[current_level]
    await current_level_function(
        call, item_id=item_id
    )
