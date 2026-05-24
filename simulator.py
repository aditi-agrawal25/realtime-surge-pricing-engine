import time
import json
import random
from kafka import KafkaProducer

# Connect to our live Kafka broker running in Docker
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

neighborhoods = ['Downtown', 'Suburbs', 'Airport', 'Financial District']

print("🚀 Starting Data Simulator... Press Ctrl+C to stop.")
while True:
    # Generate a random event
    event = {
        'passenger_id': random.randint(1000, 9999),
        'location': random.choice(neighborhoods),
        'type': random.choice(['request', 'driver_available']),
        'timestamp': time.time()
    }
    
    # Send event to the Kafka topic 'taxi-events'
    producer.send('taxi-events', event)
    print(f"📡 Dispatched Event: {event}")
    time.sleep(0.5) # Generate data every half second