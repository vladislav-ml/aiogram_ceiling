from aiogram import Bot
from aiogram.types import Message

from other.db_connect import Request
from settings import settings


async def get_list_users(message: Message, bot: Bot, request: Request):
    users = await request.get_users()
    await bot.send_message(settings.bot.admin_id, users, disable_web_page_preview=True)
