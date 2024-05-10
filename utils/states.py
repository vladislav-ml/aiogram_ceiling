from aiogram.fsm.state import State, StatesGroup


class Step(StatesGroup):
    GET_TOWN = State()
    GET_TYPE_CEILING = State()
    GET_SIZE = State()
    GET_PERIMETR = State()
    GET_LEVELING = State()
    GET_lIGHT = State()
    GET_MESSAGE = State()
