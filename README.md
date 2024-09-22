# Kafka Event Driven Architecture

## Studies based in day 3-4 of 100 Days System Design for DevOps and Cloud Engineers

### https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

### Days 1–10: Advanced Architectural Concepts.

### Day 3–4: Study Event-Driven Architecture (EDA) and set up a basic event bus using Kafka.

### Kafka basics like initial commit:
```
docker compose exec kafka bash -c "kafka-console-producer --broker-list kafka:9092 --topic test_topic"
docker compose exec kafka bash -c "kafka-console-consumer --bootstrap-server kafka:9092 --topic test_topic --from-beginning"
```

### producer_api and consumer_api (not working in all cases):
```
curl -X POST 'http://localhost:8000/send-message/' -H 'Content-Type: application/json' -d '{"message": "Hello from API!"}'
curl "http://localhost:8001/consume-message/"
```