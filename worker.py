import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
			type='fanout')
result = channel.queue_declare()
def callback(ch, method, properties, body):
	print "Received workunit %r" % body
	time.sleep(body.count('.'))
	print "Workunit finished"
	ch.basic_ack(delivery_tag= method.delivery_tag)

channel.queue_bind
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='')
channel.start_consuming()
