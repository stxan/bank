import pika
import requests
import json
import time
from xml.etree import ElementTree


# Настройки RabbitMQ
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_QUEUE = 'currency_exchange'

# Настройки API для получения курсов валют
API_URL = 'https://cbr.ru/scripts/XML_daily.asp'
#API_KEY = 'your_api_key_here'


# Функция для получения данных о курсах валют
def get_currency_rates():
    try:
        response = requests.get(f'{API_URL}')
        #print(response.text)
        xml_data = response.text
        root = ElementTree.fromstring(xml_data)
        data = {}
        for elem in root:
            for i in range(2, 5):
                key = elem[1].text
                if key not in data:
                    data[key] = []
                data[elem[1].text].append(elem[i].text)
        root = None
        return data
    except Exception as e:
        print(f"Ошибка при получении данных о курсах валют: {e}")
        return None


# Функция для отправки данных в RabbitMQ
def send_to_rabbitmq(data):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE)
        channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=json.dumps(data))
        print("Данные успешно отправлены в RabbitMQ")
        connection.close()
    except Exception as e:
        print(f"Ошибка при отправке данных в RabbitMQ: {e}")

