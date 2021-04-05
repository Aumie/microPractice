import pika,json

params = pika.URLParameters('amqps://mjfdpkrw:RbLOSU2aVKuGbouGQZJ9IbysDCh8Ejdm@cougar.rmq.cloudamqp.com/mjfdpkrw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body)
                          , properties=properties)