import matplotlib.pyplot as plt
import numpy as np


y1 = [30, 32, 40, 42, 26, 28, 30]
y2 = [25, 33, 35, 28, 29, 30, 33]
x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, label="Week One", marker='o', linestyle='-', color='#00FFFF', linewidth=2.5, markerfacecolor='white', markeredgewidth=1.5)
ax.plot(x, y2, label="Week Two", marker='o', linestyle='-', color='#FF00FF', linewidth=2.5, markerfacecolor='white', markeredgewidth=1.5)

ax.set_title("Temperature Line Plot Chart (W1 VS W2)", fontsize=16, color='white')
ax.set_xlabel("Days of the Week", fontsize=12, color='white')
ax.set_ylabel("Temperature (°C)", fontsize=12, color='white')

ax.tick_params(axis='x', colors='white', labelrotation=30)
ax.tick_params(axis='y', colors='white')

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.3)
ax.legend(facecolor='black', edgecolor='white', fontsize=10)

fig.patch.set_facecolor('black')
ax.set_facecolor('#111111')
plt.tight_layout()
plt.show()