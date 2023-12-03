import urllib
import aiormq
from config import AMQP_ADDRESS, AMQP_PORT, AMQP_USER, AMQP_VHOST, AMQP_PASSWORD


class Rabbit:

    connection = None
    channel = None
    queue_declare = None

    @classmethod
    async def connect(cls):
        if cls.connection is None:
            amqp_url = f"amqp://{urllib.parse.quote(AMQP_USER)}:{urllib.parse.quote(AMQP_PASSWORD)}@{AMQP_ADDRESS}:{AMQP_PORT}/{urllib.parse.quote(AMQP_VHOST)}"
            # connect to RabbitMQ
            cls.connection = await aiormq.connect(amqp_url)
            Rabbit.channel = await cls.connection.channel()
            cls.queue_declare = await Rabbit.channel.queue_declare(queue='0', durable=True)

    @classmethod
    async def close_connection(cls):
        if cls.connection:
            await cls.connection.close()
