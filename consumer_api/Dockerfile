FROM python:3.9-slim

WORKDIR /app

COPY consumer.py .

RUN pip install fastapi kafka-python uvicorn

CMD ["uvicorn", "consumer:app", "--host", "0.0.0.0", "--port", "8000"]
