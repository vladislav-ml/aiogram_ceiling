from aiogram.types import Message

from keyboards.keyboards_text import faq_keyboards
from utils.common import CommonClass
from utils.faq_class import Faq


async def get_faq(message: Message):
    await message.answer('Нажмите на вопрос и получите ответ.', reply_markup=faq_keyboards)


async def get_answer_on_question(message: Message):
    if not CommonClass.check_data(message.text, Faq.faq):
        await message.answer('Ошибка. Нажмите на вопрос ещё раз и получите ответ.', reply_markup=faq_keyboards)
        return
    answer = CommonClass.get_data(message.text, Faq.faq, field='answer')
    answer = f'<b>{answer}</b>'
    await message.answer(answer, parse_mode='html', reply_markup=faq_keyboards)
