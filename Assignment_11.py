import pandas as pd
import numpy as np

values = np.random.randint(1, 100, size=10)
data = pd.Series(values)

print("Generated Series:")
print(data)

print("\nValue at position 2:")
print(data.iloc[2])

filtered_data = data[data > 50]
print("\nValues above 50:")
print(filtered_data)

avg = data.mean()
mid = data.median()
low = data.min()
high = data.max()

print("\nAverage:", avg)
print("Median value:", mid)
print("Lowest value:", low)
print("Highest value:", high)