import pandas as pd
import random
from datetime import datetime, timedelta

# Simulation parameters
num_orders = 100
start_time = datetime(2025, 7, 1, 10, 0)  # store opens at 10 AM

orders = []
for i in range(num_orders):
    # Random arrival time within 4 hours
    arrival = start_time + timedelta(minutes=random.randint(0, 240))
    # Batch time: round down to nearest 30 minutes
    batch_minute = (arrival.minute // 30) * 30
    batch_time = arrival.replace(minute=batch_minute, second=0, microsecond=0)
    pick_time = random.randint(5, 10)
    delivery_time = random.randint(40, 70)
    sla_met = "Yes" if delivery_time <= 60 else "No"
    orders.append([i+1, arrival, batch_time, pick_time, delivery_time, sla_met])

df = pd.DataFrame(orders, columns=[
    "OrderID", "ArrivalTime", "BatchTime", "PickTime(mins)", "DeliveryTime(mins)", "SLA_Met"
])
df.to_csv("output.csv", index=False)

print("Simulation complete. Sample output:")
print(df.head())
print("\nAverage Delivery Time:", df["DeliveryTime(mins)"].mean(), "minutes")
print("SLA Compliance:", (df["SLA_Met"].value_counts().get("Yes",0)/len(df))*100, "%")
