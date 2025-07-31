import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("egypt_death_rates_100_rows.csv")

# Plot the line chart
plt.figure(figsize=(14, 6))
plt.plot(df["Year"], df["Death Rate (per 1000 people)"], marker='o', linestyle='-', color='darkblue')
plt.title("Death Rate in Egypt Over the Years", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Death Rate (per 1000 people)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

