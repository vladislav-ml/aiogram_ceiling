from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.keyboards_text import (leveling_keyboards, lights_keyboards,
                                      order_keyboards, towns_keyboards,
                                      types_ceilings_keyboards)
from utils.calc_ceil import CalcCeil
from utils.common import CommonClass
from utils.states import Step


async def calc_price(message: Message, bot: Bot, state: FSMContext):
    await message.answer('Выберите город, нажав на кнопку ниже.', reply_markup=towns_keyboards)
    await state.set_state(Step.GET_TOWN)


async def get_town(message: Message, state: FSMContext):
    if not CommonClass.check_data(message.text, CalcCeil.towns):
        await message.answer('Ошибка. Выберите город, нажав на кнопку ниже.', reply_markup=towns_keyboards)
        return
    await state.update_data(town=message.text)
    await message.answer('Выберите тип потолка, нажав на кнопку ниже.', reply_markup=types_ceilings_keyboards)
    await state.set_state(Step.GET_TYPE_CEILING)


async def get_type_ceiling(message: Message, bot: Bot, state: FSMContext):
    if not CommonClass.check_data(message.text.lower(), CalcCeil.types_ceilings):
        await message.answer('Ошибка! Выберите нужный тип потолка ещё раз.', reply_markup=types_ceilings_keyboards)
        return
    await state.update_data(type_ceiling=message.text)
    await message.answer('Введите площадь помещения?')
    await state.set_state(Step.GET_SIZE)


async def get_size(message: Message, bot: Bot, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Похоже вы ввели не число. Поробуйте ещё раз.')
        return
    await state.update_data(size=message.text)
    await message.answer('Введите периметр помещения?')
    await state.set_state(Step.GET_PERIMETR)


async def get_perimetr(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Похоже вы ввели не число. Поробуйте ещё раз.')
        return
    await state.update_data(perimetr=message.text)
    await message.answer('Потолок нуждается в выравнивании?', reply_markup=leveling_keyboards)
    await state.set_state(Step.GET_LEVELING)


async def get_leveling(message: Message, state: FSMContext):
    if not CommonClass.check_data(message.text, CalcCeil.leveling):
        await message.answer('Ошибка. Нажмите на кнопку ниже.', reply_markup=leveling_keyboards)
        return
    await state.update_data(leveiling=message.text)
    await message.answer('Выберите нужное освещение:', reply_markup=lights_keyboards)
    await state.set_state(Step.GET_lIGHT)


async def get_light(message: Message, state: FSMContext):
    if not CommonClass.check_data(message.text.lower(), CalcCeil.lights):
        await message.answer('Ошибка! Выберите нужный тип освещения.', reply_markup=lights_keyboards)
        return
    await state.update_data(light=message.text)
    data = await state.get_data()
    town = data['town']
    type_ceiling = data['type_ceiling']
    size = data['size']
    perimetr = data['perimetr']
    leveiling = data['leveiling']
    light = data['light']
    user_message_txt = f'Вы ввели:\n' \
        f'Город: {town}\n' \
        f'Тип потолка: {type_ceiling}\n' \
        f'Размер помещения: {size} м2\n' \
        f'Периметр помещения: {perimetr} м.\n' \
        f'Выравнивание: {leveiling}\n' \
        f'Освещение: {light}'
    await message.answer(user_message_txt)
    all_sum = CalcCeil.calc_sum(town, type_ceiling, size, perimetr, data['leveiling'], light)
    await message.answer(f'<b>Примерная стоимость установки натяжного потолка:\n {all_sum}</b>\nДля заказа нажмите на кнопку ниже - отправить контакт', reply_markup=order_keyboards, parse_mode='html')
    await state.clear()
