import asyncio

from aiogram import Bot, Dispatcher
from hand.hand import r
from aiogram.filters import Command
from aiogram.types import Message
from congif import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()

async def main() -> None:
    dp.include_router(r)
    await dp.start_polling(bot)

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:

        print('Exit')