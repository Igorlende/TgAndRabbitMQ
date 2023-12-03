import os


# configuration RabbitMQ
AMQP_USER = os.environ.get("AMQP_USER")
AMQP_PASSWORD = os.environ.get("AMQP_PASSWORD")
AMQP_ADDRESS = os.environ.get("AMQP_ADDRESS")
AMQP_VHOST = os.environ.get("AMQP_VHOST")
AMQP_PORT = int(os.environ.get("AMQP_PORT", 5672))

# configuration Telegram
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# URL for requests
EXTERNAL_API_URL = os.environ.get("EXTERNAL_API_URL")