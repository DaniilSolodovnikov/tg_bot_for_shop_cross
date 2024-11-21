from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
import os


bot = Bot(token='6440878009:AAGFGmNY9i228lQ7uKLUsKDZZyPI5SptUwM')
dp = Dispatcher(bot)

answ = dict()

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x)


@dp.message_handler(commands='Ссылки')
async def url_commands(message: types.Message):
    await message.answer('Ссылки:', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Dislike', callback_data='like_-1'))


@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('За видео 1', reply_markup=inkb)


@dp.callback_query_handlers(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    result = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = result
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


executor.start_polling(dp, skip_updates=True)