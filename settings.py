import logging
import os
from dataclasses import dataclass

from dotenv import dotenv_values


def config_logger(logger):
    logger.setLevel(logging.INFO)
    path_log = os.path.join(os.getcwd(), 'logs', 'customlog.log')
    format_str = '[%(asctime)s] %(levelname)s %(funcName)s: %(lineno)d: %(message)s'
    date_format = '%d.%m.%Y %H:%M'
    handler = logging.FileHandler(filename=path_log, mode='a', encoding='utf-8')
    handler.setFormatter(logging.Formatter(fmt=format_str, datefmt=date_format))
    logger.addHandler(handler)


logger = logging.getLogger(__name__)
config_logger(logger)


@dataclass
class Bot:
    bot_token: str
    admin_id: str
    admin_email: str
    admin_phone: str


@dataclass
class Database:
    redis_dns: str
    host: str
    port: str
    db_name: str
    user: str
    password: str


@dataclass
class Setting:
    bot: Bot
    database: Database


def get_settings(path: str):
    config = dotenv_values(path)
    return Setting(
        bot=Bot(
            bot_token=config['TOKEN'],
            admin_id=config['ADMIN_ID'],
            admin_email=config['ADMIN_EMAIL'],
            admin_phone=config['ADMIN_PHONE']
        ),
        database=Database(
            redis_dns=None,
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            db_name=config['DB_NAME'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
        )
    )


settings = get_settings('.env.dev')
