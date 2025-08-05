import logging

from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from bot.Filters.filters import IsAdmin, ChatTypeFilter

logging.basicConfig(level=logging.INFO)
admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

@admin_router.message(Command("admin"))
async def add_product(message: types.Message):
    await message.answer("Вот команды админа\n"
                         "/list_users(список пользователей)\n"
                         "/list_managers список тех поддержки")
