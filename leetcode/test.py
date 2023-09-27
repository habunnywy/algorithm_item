import matplotlib.pyplot as plt
import seaborn as sns

# Use seaborn settings for nicer plots
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

A = [100, 55, 34, 37, 49, 8, 5, 14, 11, 46, 15, 3, 32, 41, 53, 2, 33, 45, 40, 28, 9, 21, 17, 48, 31, 61, 23, 0, 35, 4, 42, 54, 56, 43, 39, 60, 29, 10, 1, 13, 51, 59, 58, 50, 47, 6, 26, 20, 24, 18, 57, 16, 52, 36, 30, 22, 12, 7, 44]
B = [0.65, 0.672, 0.678, 0.682, 0.675, 0.678, 0.679, 0.675, 0.681, 0.674, 0.682, 0.677, 0.681, 0.667, 0.667, 0.655, 0.65, 0.653, 0.651, 0.647, 0.65, 0.643, 0.652, 0.647, 0.649, 0.635, 0.638, 0.635, 0.633, 0.628, 0.623, 0.623, 0.619, 0.614, 0.625, 0.606, 0.615, 0.608, 0.615, 0.606, 0.597, 0.599, 0.591, 0.602, 0.6, 0.594, 0.587, 0.581, 0.592, 0.578, 0.585, 0.587, 0.571, 0.574, 0.575, 0.571, 0.571, 0.581, 0.551]

# Create X and Y data points
data_points = [(i+4, a) for i, a in enumerate(A)]

# Split X and Y coordinates
x_values, y_values = zip(*data_points)

# Plot the transformed curve
plt.figure(figsize=(12, 7))
plt.plot(x_values, B, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
plt.xlabel('channel_nums', fontsize=14)
plt.ylabel('Accuracy', fontsize=14)
plt.title('Search line results--Whole brain', fontsize=16, fontweight='bold')

# Modify x-ticks to appear every 5 units
plt.xticks(range(min(x_values), max(x_values)+1, 5))

plt.show()
