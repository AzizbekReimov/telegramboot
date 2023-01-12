from aiogram.dispatcher.filters.state import StatesGroup, State

class Server(StatesGroup):
    server_name = State()
    server_player = State()
    server_ball_over = State()
