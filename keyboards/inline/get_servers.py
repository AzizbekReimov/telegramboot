from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from data.config import server_keys, server_namee, servers

menu_cd = CallbackData("show_menu", "level", "item_id")
add_serverr = CallbackData("add_server", "item_id")

def make_callback_data(level, item_id="0"):
    return menu_cd.new(
        level=level, item_id=item_id
    )



async def Servers():

    CURRENT_LEVEL = 0

    markub = InlineKeyboardMarkup(row_width=1)
    serverss = server_keys
    for server in serverss:
        server_players = len(servers[server]['players'])

        button_text = f"{server}: {server_players}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, item_id=server)

        markub.insert(InlineKeyboardButton(text=button_text, callback_data=callback_data))

    
    return markub

def Server(item_id):
    CURRENT_LEVEL = 1
    markub = InlineKeyboardMarkup(row_width=1)
    markub.row(
        InlineKeyboardButton(
            text="serverga qoshilish",
            callback_data=make_callback_data(
                level= CURRENT_LEVEL + 1,
                item_id="add_server"
            ),
        )
    )

    markub.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1,
            ),
        )
    )
    return markub

def Cancel_Server():
    CURRENT_LEVEL = 2
    markub = InlineKeyboardMarkup(row_width=1)
    markub.row(
        InlineKeyboardButton(
            text="serverdan chiqish",
            callback_data=add_serverr.new(
                item_id="cancel_server"
            ),
        )
    )
    return markub
