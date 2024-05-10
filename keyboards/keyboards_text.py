from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from utils.calc_ceil import CalcCeil
from utils.common import CommonClass
from utils.faq_class import Faq

menu_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Рассчитать стоимость'
            ),
            KeyboardButton(
                text='Сделать заказ',
            ),
        ],
        [
            KeyboardButton(
                text='Отправить сообщение'
            ),
            KeyboardButton(
                text='Наши контакты'
            )
        ],
        [
            KeyboardButton(
                text='Частые вопросы'
            )
        ]
    ], resize_keyboard=True
)

order_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Отправить контакт',
                request_contact=True
            )
        ]
    ], resize_keyboard=True
)

leveling_keyboards = CommonClass.get_keyboard_divide(CalcCeil.leveling, 2)

types_ceilings_keyboards = CommonClass.get_keyboard_divide(CalcCeil.types_ceilings)

lights_keyboards = CommonClass.get_keyboard_divide(CalcCeil.lights, 2)

towns_keyboards = CommonClass.get_keyboard_divide(CalcCeil.towns, 2)

faq_keyboards = CommonClass.get_keyboard_divide(Faq.faq, 1)
