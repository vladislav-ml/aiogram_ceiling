from typing import Optional

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class CommonClass:

    @classmethod
    def check_data(cls, key: str, elements: dict) -> bool:
        res = False
        for d in elements:
            value = d.get('name', '')
            if value.lower() == key.lower():
                res = True
                break
        return res

    @classmethod
    def get_data(cls, key: str, elements: dict, field: str = 'price') -> Optional[int]:
        res = None
        for d in elements:
            value = d.get('name', '')
            if value.lower() == key.lower():
                res = d.get(field)
                break
        return res

    @classmethod
    def get_keyboard_divide(cls, data: dict, chunk: int = 3) -> ReplyKeyboardMarkup:
        button_list = [KeyboardButton(text=x['name'].capitalize()) for x in data]
        button_divide = [button_list[i: i + chunk] for i in range(0, len(button_list), chunk)]
        keyboard = ReplyKeyboardMarkup(keyboard=button_divide, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажмите на кнопку')
        return keyboard
