from aiogram.fsm.state import StatesGroup, State


class FormStates(StatesGroup):
    name = State()
    age = State()
    gender = State()
    city = State()
    description = State()
    photo = State()