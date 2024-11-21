from aiogram import Bot
from aiogram import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()


bot = Bot(token='6440878009:AAGFGmNY9i228lQ7uKLUsKDZZyPI5SptUwM')
dp = Dispatcher(bot, storage=storage)
