from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


from .routers import router
from .config import bot_settings


class BotFactory:

    @staticmethod
    async def start_bot():
        dp = Dispatcher()
        dp.include_router(router)

        bot = Bot(
            bot_settings.token,
            parse_mode=ParseMode.HTML
        )
        await dp.start_polling(bot)
