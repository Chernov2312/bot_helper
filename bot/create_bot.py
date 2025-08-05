import logging

from aiogram import Bot, Dispatcher, types

from bot.common.commands import commands_user
from bot.handlers.private_admin_handler import admin_router
from bot.handlers.private_user_handler import user_router
from config.Config import settings

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.BOT_TOKEN)
bot.my_admins_list = [1888207571]

dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(admin_router)


async def start_bot():

    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=commands_user, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    logging.info("Бот запущен.")


async def stop_bot():
    try:
        logging.info("Бот остановлен.")
    except:
        pass