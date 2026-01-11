from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message) -> None:
    await msg.answer_sticker(
        'CAACAgIAAxkBAAEQKeZpWNkujun8FTLBfNDrhQQNtrY-0wACBQADwDZPE_lqX5qCa011OAQ'
    )
    await msg.answer(
        f'Привет, <b>{msg.from_user.full_name}</b>!\nЯ помогу найти тебе пару или друзей. 👫',
        parse_mode='HTML',
    )


@router.message(Command('help'))
async def help_handler(msg: Message) -> None:
    await msg.answer(
        f'Вы нажали команду /help',
        parse_mode='HTML',
    )


@router.message(F.text == 'Давай начнём!')
async def lets_start_handler(msg: Message) -> None:
    await msg.answer('Как тебя зовут?')
