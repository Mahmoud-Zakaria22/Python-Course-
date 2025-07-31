import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("egypt_death_rates_100_rows.csv")

# Select features and target
X = df[["Health Expenditure (% of GDP)"]]
y = df["Life Expectancy (years)"]

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Actual")
plt.plot(X, y_pred, color="red", linewidth=2, label="Regression Line")
plt.title("Linear Regression: Health Expenditure vs Life Expectancy")
plt.xlabel("Health Expenditure (% of GDP)")
plt.ylabel("Life Expectancy (years)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Output model parameters
print(f"Slope (coefficient): {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"R² Score: {model.score(X, y):.4f}")





