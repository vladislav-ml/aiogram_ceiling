import asyncio

import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from handlers.admin import get_list_users
from handlers.basic import (download_price, get_contact_order, get_message,
                            order, send_message_admin, show_contacts,
                            show_menu)
from handlers.calc import (calc_price, get_leveling, get_light, get_perimetr,
                           get_size, get_town, get_type_ceiling)
from handlers.faq import get_answer_on_question, get_faq
from middleware.db_middleware import DbSession
from other.commands_bot import set_commands
from settings import logger, settings
from utils.states import Step


async def start_bot(bot: Bot):
    await set_commands(bot)
    # me = await bot.get_me()
    # await bot.send_message(settings.bot.admin_id, f'Бот <b>{me.first_name}</b> запущен!', parse_mode='html')
    logger.info('Бот запущен.')


async def stop_bot(bot: Bot):
    # me = await bot.get_me()
    # await bot.send_message(settings.bot.admin_id, f'Бот <b>{me.first_name}</b> остановлен!', parse_mode='html')
    logger.info('Бот остановлен.')


async def create_pool(host, user, password, database, port):
    return await asyncpg.create_pool(host=host, user=user, password=password, database=database, port=port)


async def main():
    bot = Bot(settings.bot.bot_token)
    dp = Dispatcher()

    # db
    pooling = await create_pool(settings.database.host, settings.database.user, settings.database.password, settings.database.db_name, settings.database.port)

    dp.callback_query.middleware(DbSession(pooling))
    dp.message.middleware(DbSession(pooling))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # handlers faq
    dp.message.register(get_faq, F.text == 'Частые вопросы')
    dp.message.register(get_answer_on_question, F.text.regexp(r'[а-яА-Я ]+\?$'))

    # handlers admin
    dp.message.register(get_list_users, F.from_user.id == int(settings.bot.admin_id), Command(commands=['admin']))

    # handlers basic
    dp.message.register(calc_price, F.text.lower() == 'рассчитать стоимость')
    dp.message.register(get_type_ceiling, Step.GET_TYPE_CEILING)
    dp.message.register(get_size, Step.GET_SIZE)
    dp.message.register(get_perimetr, Step.GET_PERIMETR)
    dp.message.register(get_leveling, Step.GET_LEVELING)
    dp.message.register(get_light, Step.GET_lIGHT)
    dp.message.register(get_town, Step.GET_TOWN)
    dp.message.register(show_menu, Command(commands=['start']))
    dp.message.register(download_price, F.text.lower() == 'скачать прайс')
    dp.message.register(order, F.text.lower() == 'сделать заказ')
    dp.message.register(get_message, Step.GET_MESSAGE)
    dp.message.register(send_message_admin, F.text.lower() == 'отправить сообщение')
    dp.message.register(get_contact_order, F.content_type == 'contact')
    dp.message.register(show_contacts, F.text.lower() == 'наши контакты')
    dp.message.register(show_menu, F.text)

    await dp.start_polling(bot)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
