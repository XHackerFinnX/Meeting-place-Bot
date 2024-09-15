from aiogram.types import Message

async def telegram_name_users(message: Message):
    
    fname = str(message.chat.first_name)
    lname = str(message.chat.last_name)
    uname = '@' + str(message.chat.username)
    
    return fname, lname, uname