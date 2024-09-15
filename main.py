import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from log.log import log_message
from config.config import config

from handler import user_commands

async def main() -> None:
    bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    dp.include_routers(
        user_commands.router
    )
    
    print('Бот запущен!')
    
    await log_message("System", "admin", "Запуск Бота!")
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())