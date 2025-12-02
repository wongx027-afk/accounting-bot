import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = 8558690628:AAG_IU-8txAONB0VsCkT6qnODF0qhUm3Mgg

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def main_handler(message: types.Message):
    text = message.text

    # 测试机器人是否工作
    await message.reply(f"机器人已上线，你发送了：{text}")

if __name__ == "__main__":
    executor.start_polling(dp)
