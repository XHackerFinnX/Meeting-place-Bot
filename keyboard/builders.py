from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def profile(text: str | list):
    builder = ReplyKeyboardBuilder()
    
    if isinstance(text, str):
        text = [text]
        
    [builder.button(text=txt) for txt in text]
    
    return builder.as_markup(resize_keyboard = True)