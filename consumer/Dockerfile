FROM python:3.9-slim
WORKDIR /app
COPY consumer.py /app/
RUN pip install kafka-python
CMD ["python", "consumer.py"]
