from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Рассчитать стоимость',
                callback_data='calc_price'
            ),
            InlineKeyboardButton(
                text='Сделать заказ',
                callback_data='order'
            ),
            InlineKeyboardButton(
                text='Перейти на сайт',
                url='https://vladhistory.com'
            )
        ]
    ]
)

contact_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Перейти на сайт',
                url='https://apartment-stroy.ru'
            ),
            InlineKeyboardButton(
                text='Прочитать отзывы',
                url='https://apartment-stroy.ru/otzyvy1'
            )
        ]
    ]
)

leveling_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Да',
                callback_data='leveling_yes'
            ),
            InlineKeyboardButton(
                text='Нет',
                callback_data='leveling_no'
            )
        ]
    ]
)
