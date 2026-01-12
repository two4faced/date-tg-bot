from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.utils import lets_start_keyboard

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message) -> None:
    await msg.answer_sticker(
        'CAACAgIAAxkBAAEQKeZpWNkujun8FTLBfNDrhQQNtrY-0wACBQADwDZPE_lqX5qCa011OAQ'
    )
    await msg.answer(
        f'Привет, <b>{msg.from_user.full_name}</b>!\nЯ помогу найти тебе пару или друзей. 👫',
        parse_mode='HTML',
        reply_markup=lets_start_keyboard(),
    )


@router.message(Command('help'))
async def help_handler(msg: Message) -> None:
    await msg.answer(
        'Вы нажали команду /help',
        parse_mode='HTML',
    )
