# World Population Growth Analysis
# Simple data visualization project to analyze population trends

import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with a real dataset later!)
data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Population (Billion)": [6.14, 6.45, 6.92, 7.35, 7.79]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Population (Billion)"], marker='o', linestyle='-', color='teal')

# Customize the plot
plt.title("World Population Growth (2000-2020)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population (Billion)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.savefig('population_growth.png')  # Save the plot as an image
plt.show()

# Print the data
print(df)
