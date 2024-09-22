from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(10):
    message = {'message': f'Hello Kafka {i}'}
    producer.send('test_topic', message)
    print(f'Sent: {message}')
    time.sleep(1)

producer.flush()
