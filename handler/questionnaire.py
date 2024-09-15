from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form

from keyboard.builders import profile

router = Router()

#@router.message(Command('start'))
#async def fill_profile(message: Message, state: FSMContext):
#    
#    await state.set_state(Form.name)
#    await message.answer(
#        text='Введите своё имя:'
#        )
    
#@router.message(Form.name)
