import os

import openai
import asyncio
from aiogram import Bot, Dispatcher, types

from example import example

bot = Bot(token='6779695847:AAElbubIHe31zTw9XP5cuwtSJk_zz5s37jk')

dp = Dispatcher()
openai.api_key = os.environ['OPENAI_API_KEY']
example()
@dp.message()
async def gpt(message: types.Message):
    response = openai.Completion.create(model="text-davinci-003",
                                         prompt=message.text,
                                         temperature=0.5,
                                         max_tokens=1024,
                                         top_p=1,
                                         frequency_penalty=0.0,
                                         presence_penalty=0.0)
    await message.reply(response.choices[0].text)
async def main(): 
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
