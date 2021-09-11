from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration_states(StatesGroup):
    enter_email = State()


class Meeting_states(StatesGroup):
    promeshytok_state = State()
