from config import EXTERNAL_API_URL
import aiohttp
from globals import LastMessage
from rabbit import Rabbit


async def consume_rabbitmq():

    consume_ok = await Rabbit.channel.basic_consume(
        Rabbit.queue_declare.queue, callback, no_ack=True
    )


async def callback(message):
    message = message.body.decode()
    print(f"Received message from RabbitMQ: {message}", flush=True)

    # Command processing "print"
    if message.lower() == 'print':
        print_last_message()

    # Command processing "send"
    elif message.lower() == 'send':
        await send_to_external_api(message)


async def send_to_external_api(message):
    try:
        async with aiohttp.ClientSession() as session:
            payload = {'message': message}
            async with session.post(EXTERNAL_API_URL, json=payload) as response:
                print(f"Sent message to external API: {message}", flush=True)
                print(f"API response status: {response.status}", flush=True)
                print(f"API response: {await response.text()}", flush=True)
    except Exception as e:
        print(f"An error occurred while sending message to external API: {e}", flush=True)


def print_last_message():
    print(f"Last message from Telegram: {LastMessage.message}", flush=True)