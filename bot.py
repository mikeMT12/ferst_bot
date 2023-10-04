# 1. На команду /start, отправленную боту, ответим приветствием.
# 2. На команду /sendcat - отправим 😺
# 3. На команду /senddog - отправим 🐶
import os
import logging
import aiogram
import dotenv
dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot=bot)


@dp.message_handler(commands='start')
async def start(message: aiogram.types.Message):
    await message.answer('Привет!')


@dp.message_handler(commands='send')
async def send_cat(message: aiogram.types.Message):

    ANIMAL_EMOJIS = {
        "cat": "😺",
        "dog": "🐶",
        "zebra": "🦓",
        "dragon": "🐲"
    }
    animal = message.get_args()
    if animal in ANIMAL_EMOJIS:
        await message.answer(ANIMAL_EMOJIS[animal])
    else:
        await message.answer("Нет такого аргумента!\nДоступны:\n" + '\n'.join(ANIMAL_EMOJIS.keys()))


async def send_dog(message: aiogram.types.Message):
    await message.answer('🐶')

dp.register_message_handler(send_dog, commands='senddog')


@dp.message_handler(commands='help')
async def help(message: aiogram.types.Message):
    await message.answer('/start - Начать работу с ботом\n'
                         '/help - Помощь по боту\n'
                         '/send [животное] - прислать эмодзи животного')


@dp.message_handler(commands="dice")
async def cmd_dice(message: aiogram.types.Message):
    sent_dice = await message.answer_dice(emoji="🏀")
    print(f"Пользователь {message.from_user.full_name} выбил {sent_dice.dice.value} очков.")


@dp.message_handler()
async def echo(message: aiogram.types.Message):
    if message.text:
        await message.answer(message.text)
    else:
        await message.answer(message.caption)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    aiogram.executor.start_polling(dispatcher=dp)
