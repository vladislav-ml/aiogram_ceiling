import os

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message

from keyboards.keyboards_inline import contact_keyboards
from keyboards.keyboards_text import menu_keyboards, order_keyboards
from other.db_connect import Request
from settings import logger, settings
from utils.states import Step


async def show_menu(message: Message, bot: Bot):
    await message.answer('Здравствуйте! Выберите один из пунктов меню.', reply_markup=menu_keyboards)


async def show_contacts(message: Message, bot: Bot):
    admin_mes_me = ''
    admin_username = None
    try:
        admin_id = settings.bot.admin_id
        admin_info = await bot.get_chat(admin_id)
        admin_username = admin_info.username
    except Exception as e:
        logger.error(f'{type(e)} - {e}')

    if admin_username:
        admin_mes_me = f'Написать: https://t.me/{admin_username}'

    message_txt = '<b>Устанавливаем натяжные потолки в Москве и Московской области.' \
    '</b> Работаем по договору.\n<b>Наши контакты</b>\n' \
    f'Телефон: <b>{settings.bot.admin_phone}</b>\n' \
    f'Email: <b>{settings.bot.admin_email}</b>\n{admin_mes_me}'
    await message.answer(message_txt, parse_mode='html', reply_markup=contact_keyboards)


async def download_price(message: Message, bot: Bot):
    path_file = os.path.join(os.getcwd(), 'downloads', 'potolki_03_04_2024_13_40_07.pdf')
    await bot.send_document(message.from_user.id, document=FSInputFile(path_file), caption='Цены на натяжные потолки')


async def order(message: Message):
    await message.answer('Нажмите на кнопку ниже - отправить контакт.', reply_markup=order_keyboards)


async def get_contact_order(message: Message, bot: Bot, request: Request):
    user_id = message.contact.user_id
    user_first_name = message.contact.first_name
    user_phone = message.contact.phone_number
    user_url = get_user_url(message)
    await request.add_user_contact(user_id, user_first_name, user_phone, user_url)
    await message.answer('Принято. Мы вам перезвоним.', reply_markup=menu_keyboards)
    me = await bot.get_me()
    message_admin = f'Сообщение от бота: {me.first_name}.\nПолучен контакт.\n' \
    f'Имя: <b>{user_first_name}</b>\n' \
    f'Телефон: <b>{user_phone}</b>\n' \
    f'Ссылка на профиль: <b>{user_url}</b>'
    await bot.send_message(settings.bot.admin_id, message_admin, parse_mode='html')


async def send_message_admin(message: Message, bot: Bot, state: FSMContext):
    await message.answer('<b>Введите сообщение ниже</b>', reply_markup=None, parse_mode='html')
    await state.set_state(Step.GET_MESSAGE)


async def get_message(message: Message, bot: Bot, state: FSMContext):
    if not message.text:
        await message.answer('Ошибка. Введите сообщение ещё раз')
        return
    await message.answer('Ваше сообщение принято. Ждите. Мы вам ответим.', reply_markup=menu_keyboards)
    me = await bot.get_me()
    user_url = get_user_url(message)
    message_admin = f'Сообщение от бота: {me.first_name}.\n' \
    f'Имя: <b>{message.from_user.first_name}</b>\n' \
    f'Ссылка на профиль: <b>{user_url}</b>\n' \
    f'Текст сообщения:\n<b>{message.text}</b>'
    await bot.send_message(settings.bot.admin_id, message_admin, parse_mode='html')
    await state.clear()


def get_user_url(message):
    user_url = f'https://t.me/{message.from_user.username}' if message.from_user.username else f'tg://openmessage?user_id={message.from_user.id}'
    return user_url
