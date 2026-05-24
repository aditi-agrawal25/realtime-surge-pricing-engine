import streamlit as st
import redis
import time
import pandas as pd

# Connect to our fast Redis cache database
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

st.title("⚡ Real-Time Surge Pricing Dashboard")
st.write("Reading streaming supply-demand metrics live from Redis memory layer...")

# Create an empty layout placeholder that updates continuously
placeholder = st.empty()

neighborhoods = ['Downtown', 'Suburbs', 'Airport', 'Financial District']

while True:
    data = []
    for loc in neighborhoods:
        reqs = r.hget(loc, 'requests') or 0
        drvs = r.hget(loc, 'drivers') or 0
        surge = r.hget(loc, 'surge_price') or 1.0
        
        data.append({
            "Location Zone": loc,
            "Active Requests (Demand)": int(reqs),
            "Available Drivers (Supply)": int(drvs),
            "Current Surge Multiplier": f"{surge}x"
        })
    
    df = pd.DataFrame(data)
    
    # Wipe the old table and re-render the fresh data instantly
    with placeholder.container():
        st.dataframe(df, use_container_width=True)
        
    time.sleep(1) # Refresh window every 1 second