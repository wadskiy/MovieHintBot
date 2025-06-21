from aiogram import Bot, Dispatcher, types, executor
import asyncio
import os
import random

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

movies = [
    "Inception", "The Matrix", "Interstellar",
    "Pulp Fiction", "The Godfather", "Fight Club"
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("🎬 Привет! Напиши /movie чтобы получить рекомендацию!")

@dp.message_handler(commands=['movie'])
async def movie_hint(message: types.Message):
    await message.reply(f"🎥 Советую посмотреть: {random.choice(movies)}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
