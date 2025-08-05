import logging

from aiogram import Router
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.state import State
from aiogram.types import Message


logging.basicConfig(level=logging.INFO)
user_router = Router()
def get_user_info():
    nick_name = State()
    phone_number = State()
    user_email = State()

@user_router.message(Command('start'))
async def cmd_start(message: Message):
    await message.reply("Приветствую вас, Я чат gpt4 вы можете генерировать картинки, и пасть тексты и многое другое!")
    logging.info("Приветствие")

