# realtime-surge-pricing-engine
# Real-Time Surge Pricing Engine

Most data science projects use static CSV files. I wanted to build something that handles data the way companies like Uber or Swiggy do—live, as it happens. 

This project is a real-time data pipeline that simulates a ride-sharing ecosystem. It streams live traffic data, processes it instantly, and calculates dynamic surge pricing multipliers based on neighborhood supply and demand.

## How the Data Flows
1. **`simulator.py`**: A script that mimics thousands of drivers and riders sending live location pings.
2. **Apache Kafka (Docker)**: Acts as the high-speed data highway, collecting all these streaming pings in perfect order.
3. **`processor.py`**: The brain. It reads from Kafka, tracks active demand numbers inside a **Redis** cache, and runs a math formula to instantly update the neighborhood's surge price.
4. **`app.py`**: A **Streamlit** web dashboard that reads the live numbers from Redis and updates a visual table on your screen every single second.

## The Tech Stack
* **Language:** Python
* **Streaming & Infrastructure:** Apache Kafka, Redis, Docker Compose
* **Frontend Dashboard:** Streamlit, Pandas

## How to Run It Locally

### Prerequisites
Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) and Python installed.

1. **Start Kafka & Redis:**
   ```bash
   docker-compose up -d
   Install Libraries:

Bash
pip install kafka-python-ng redis streamlit pandas
Run the system (Open 3 separate terminal tabs):

Terminal 1: python processor.py

Terminal 2: streamlit run app.py

Terminal 3: python simulator.py

What I Learned From Building This
Handling Live Streams: Learned how to process data that doesn't just sit still in an Excel sheet.

Why Caching Matters: Used Redis because standard databases are too slow to calculate and update prices in milliseconds.

System Decoupling: Used Kafka to make sure that even if the front-end dashboard lags, incoming traffic data is never dropped.


---

### Push the changes:
Run your commands one last time to update it on GitHub:
```bash
git add README.md
git commit -m "docs: simplify readme to sound more human"
git push origin main
