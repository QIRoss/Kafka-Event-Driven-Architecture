from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json

app = FastAPI()

class Message(BaseModel):
    message: str

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.post("/send-message/")
async def send_message(msg: Message):
    producer.send('test_topic', {'message': msg.message})
    return {"status": "Message sent successfully"}
