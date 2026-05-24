import json
from kafka import KafkaConsumer
import redis

# Listen to Kafka topic and connect to Redis
consumer = KafkaConsumer('taxi-events', bootstrap_servers=['localhost:9092'])
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("🧠 Brain Processor Active... Watching live supply & demand.")

for message in consumer:
    event = json.loads(message.value.decode('utf-8'))
    loc = event['location']
    event_type = event['type']
    
    # Update live Redis counts based on incoming streaming logs
    if event_type == 'request':
        r.hincrby(loc, 'requests', 1)
    elif event_type == 'driver_available':
        r.hincrby(loc, 'drivers', 1)
        
    # Fetch latest calculations
    reqs = int(r.hget(loc, 'requests') or 0)
    drvs = int(r.hget(loc, 'drivers') or 0)
    
    # Math Engine: Simple Surge Pricing Algorithm (Demand / Supply ratio)
    if drvs == 0 and reqs > 0:
        surge = 3.0  
    elif drvs > 0:
        ratio = reqs / drvs
        if ratio > 1.2:
            surge = round(min(3.0, 1.0 + (ratio * 0.25)), 2)
        else:
            surge = 1.0
    else:
        surge = 1.0
        
    # Cache the dynamic multiplier directly back into Redis memory
    r.hset(loc, 'surge_price', surge)
    print(f"📊 {loc:20} -> Demand: {reqs:3} | Supply: {drvs:3} | SURGE: {surge}x")