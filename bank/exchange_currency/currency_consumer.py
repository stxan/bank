"""import pika
import json
from .models import CurrencyRate

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='currency_exchange')


def callback_func(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    print("called consumer")
    for key in data:
        currency_code = str(key)
        rate = float(data[key][2].replace(',', '.')) / float(data[key][0].replace(',', '.'))
        currency_name = data[key][1]
        try:
            currency_rate = CurrencyRate.objects.get(currency_code=str(currency_code))
            currency_rate.rate = rate
            currency_rate.currency_name = currency_name
            currency_rate.save()
        except CurrencyRate.DoesNotExist:
            CurrencyRate.objects.create(currency_code=currency_code, rate=rate, currency_name=currency_name)


channel.basic_consume(queue='currency_exchange', on_message_callback=callback_func, auto_ack=True)

print('Waiting for currency rates. To exit press CTRL+C aaaa')
channel.start_consuming()"""