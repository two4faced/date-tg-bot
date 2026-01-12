from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.fsm.form_states import FormStates
from src.utils import gender_keyboard, no_desc_keyboard


router = Router()


@router.message(F.text == 'Давай начнём!')
async def lets_start_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer('Как тебя зовут? Это имя будет отображаться в твоей анкете')
    await state.set_state(FormStates.name)


@router.message(FormStates.name)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Сколько тебе лет?')
    await state.set_state(FormStates.age)


@router.message(FormStates.age)
async def get_age(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer('Теперь определимся с полом', reply_markup=gender_keyboard())
    await state.set_state(FormStates.gender)


@router.message(FormStates.gender)
async def get_gender(msg: Message, state: FSMContext):
    if msg.text == 'Я девушка':
        await state.update_data(gender='ж')
    if msg.text == 'Я парень':
        await state.update_data(gender='м')

    await msg.answer('Из какого ты города или в каком городе ищешь друзей?')
    await state.set_state(FormStates.city)


@router.message(FormStates.city)
async def get_city(msg: Message, state: FSMContext):
    await state.update_data(city=msg.text)
    await msg.answer(
        'Теперь расскажи пару слов о себе и кого хочешь найти', reply_markup=no_desc_keyboard()
    )
    await state.set_state(FormStates.description)


@router.message(FormStates.description)
async def get_description(msg: Message, state: FSMContext):
    if msg.text == 'Не хочу заполнять информацию о себе':
        await state.update_data(description='')
    else:
        await state.update_data(description=msg.text)

    await msg.answer('Теперь пришли фото для своей анкеты')
    await state.set_state(FormStates.photo)


@router.message(FormStates.photo, F.photo)
async def get_photo(msg: Message, state: FSMContext):
    await state.update_data(photo=msg.photo[-1].file_id)
    await msg.answer('Твоя анкета готова! 🎉\nВот как она выглядит:')

    data = await state.get_data()
    print(data)
    await msg.answer_photo(
        photo=data['photo'],
        caption=f'{data["name"]}, {data["age"]}, {data["city"]} \n\n{data["description"]}',
    )

    await state.clear()


@router.message(FormStates.photo)
async def check_send_photo(msg: Message):
    await msg.answer('Отправь фото для анкеты')
