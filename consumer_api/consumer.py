from fastapi import FastAPI
from kafka import KafkaConsumer

app = FastAPI()

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group'
)

@app.get("/consume-message/")
async def consume_message():
    # Consume a single message
    for message in consumer:
        return {"message": message.value.decode('utf-8')}
