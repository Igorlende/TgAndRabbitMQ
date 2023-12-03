import time
import asyncio
from handlers import dp
from waiting_rabbit import consume_rabbitmq
from rabbit import Rabbit


async def main():
    # wait for running in docker rabbitmq
    time.sleep(30)
    print("starting..", flush=True)
    await Rabbit.connect()
    await consume_rabbitmq()
    await dp.start_polling()
    await Rabbit.close_connection()


if __name__ == '__main__':
    asyncio.run(main())

