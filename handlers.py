from config import TELEGRAM_BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from globals import LastMessage
import aiormq
from rabbit import Rabbit


# create bot and dispatcher for aiogram
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(content_types=types.ContentType.ANY)
async def save_last_message(message: types.Message):
    LastMessage.message = message.text
    if message.text == 'print':
        await Rabbit.channel.basic_publish(
            body=message.text.encode(),
            exchange='',
            routing_key='0',
            properties=aiormq.spec.Basic.Properties(
                delivery_mode=2,  # Making a message to those experiencing a broker restart
            ),
        )
    elif message.text == 'send':
        await Rabbit.channel.basic_publish(
            body=message.text.encode(),
            exchange='',
            routing_key='0',
            properties=aiormq.spec.Basic.Properties(
                delivery_mode=2,  # Making a message to those experiencing a broker restart
            ),
        )
    await message.reply('recorded as last')