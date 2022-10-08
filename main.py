import asyncio
from aiogram import Bot, Dispatcher, types
from tube_stream_loader import yt_stream
from advice import nice_advice


with open("token.txt", "r") as f:
    token = f.read()

bot = Bot(token=token)

dp = Dispatcher(bot)


@dp.message_handler(commands=["tubeload"])
async def youtube_loader(message: types.Message):
    url = message.get_full_command()[1].split(' ')
    stream = yt_stream(url)
    for title, file in stream:
        await message.answer_audio(file.getvalue(), title=title + ".mp3")


@dp.message_handler(commands=["advice"])
async def adv(message: types.Message):
    await message.answer(nice_advice())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())