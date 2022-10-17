from aiogram import types
from .control import dp
from .get_data import fetch, key
from .keyboards import kb1, kb2, kb3


@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    await message.reply(
        text=f"Hi bot {message.from_user.full_name}",
        reply_markup=kb1()
    )


@dp.message_handler(text='Продукция 📦')
async def gets(message: types.Message):
    await message.answer(f'Вибрайте:', reply_markup=kb2())


@dp.message_handler(text="ВСТРАИВАЕМАЯ ТЕХНИКА")
async def gets1(message: types.Message):
    await key()
    await message.answer(f'продукт:', reply_markup=kb3())


@dp.message_handler(content_types=types.ContentType.TEXT)
async def gets2(message: types.Message):
    message1 = message.text
    data = await fetch()
    for x in data:
        name = x['name']
        img = x['img']
        description = x['description']
        if message1 == x['name']:
            await message.answer_photo(img)
            await message.answer(f'{name}'
                                 f'\n{description}'
                                 )
