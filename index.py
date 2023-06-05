from aiogram.dispatcher.filters.state import State,StatesGroup

class Register(StatesGroup):
    name = State()
    last_name = State()
    number = State()
    location = State()
    school = State()
    cheeck = State()