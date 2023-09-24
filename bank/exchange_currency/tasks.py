import json

import dramatiq
import time
from exchange_currency.getting_currency import get_currency_rates, send_to_rabbitmq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pika
import os
import threading


#RABBITMQ_HOST = 'localhost'
#RABBITMQ_PORT = 5672
#RABBITMQ_QUEUE = 'currency_exchange'

#API_URL = 'https://cbr.ru/scripts/XML_daily.asp'

#broker = RabbitmqBroker(host="localhost")

#dramatiq.set_broker(broker)


@dramatiq.actor
def process():
    currency_data = get_currency_rates()
    if currency_data:
        send_to_rabbitmq(currency_data)


"""@dramatiq.actor
def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='currency_exchange')
    channel.basic_consume(queue='currency_exchange', on_message_callback=callback_func, auto_ack=True)
    print('Waiting for currency rates. To exit press CTRL+C aaaa')
    channel.start_consuming()"""


#consume_thread = threading.Thread(target=consume)
#consume_thread.start()
#timeout_seconds = 30
#consume_thread.join(timeout=timeout_seconds)
#if consume_thread.is_alive():
#    print("Время выполнения истекло. Останавливаем поток.")
#    consume_thread.stop()

if __name__ == "__main__":
    print("called process")
    scheduler = BlockingScheduler()
    scheduler.add_job(
        process.send,
        CronTrigger.from_crontab("* * * * *"),
    )
    #scheduler.add_job(
     #   consume.send,
      #  CronTrigger.from_crontab("* * * * *"),
    #)
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()