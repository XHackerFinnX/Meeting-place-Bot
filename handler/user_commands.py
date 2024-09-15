from aiogram.types import Message
from aiogram import Router
from aiogram import html
from aiogram.filters import CommandStart, Command

from log.log import log_message

from data.user import sql_users_add

from handler.bot_messages import telegram_name_users

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(text= f"Hello, {html.bold(message.from_user.id)}!")
    
    await log_message("Users", message.from_user.id, "Выполнил команду - /start")
    
    fname, lname, uname = await telegram_name_users(message)
    
    await sql_users_add(message.from_user.id, fname, lname, uname)
    
    
@router.message(Command(commands=['help']))
async def command_help_handler(message: Message) -> None:
    
    await message.answer(text= "Какая нужна помощь?")
    
    await log_message("Users", message.from_user.id, "Выполнил команду - /help")