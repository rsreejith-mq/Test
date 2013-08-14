import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='new_queue',
		durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World."
channel.exchange_declare(exchange='logs',
			type='fanout')
channel.basic_publish(exchange='logs', 
		routing_key='',
		body=message)
print "Message " + message + " sent"
connection.close()
