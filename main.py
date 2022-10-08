import asyncio
from aiogram import Bot, Dispatcher, types
from tube_loader import yt_loader, direct
import os
from advice import nice_advice

bot = Bot(token="")

dp = Dispatcher(bot)

@dp.message_handler(commands=["ytd"])
async def youtube_loader(message: types.Message):
    url = message.get_full_command()[1].split(' ')
    yt_loader(url)
    file_ext = r".mp3"
    for f in [x for x in os.listdir(direct) if x.endswith(file_ext)]:
        await message.answer_audio(open(f"{direct}/{f}", "rb"))
        os.remove(f"{direct}/{f}")

@dp.message_handler(commands=["advice"])
async def adv(message: types.Message):
    await message.answer(nice_advice())

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())