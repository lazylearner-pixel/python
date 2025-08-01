import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(10, 100, size=4)

# Heatmap data
heatmap_data = np.random.rand(6, 6)

# Create figure with multiple subplots
fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(2, 3, hspace=0.4, wspace=0.4)

# Subplot 1: Line plot
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(x, y1, label='sin(x)', color='blue')
ax1.plot(x, y2, label='cos(x)', color='red')
ax1.set_title("Line Plot: sin(x) & cos(x)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.legend()

# Subplot 2: Scatter plot
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(x, y3, color='green', marker='o', alpha=0.7)
ax2.set_title("Scatter Plot: sin(x)*cos(x)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

# Subplot 3: Bar plot
ax3 = fig.add_subplot(gs[0, 2])
ax3.bar(categories, values, color=['orange', 'purple', 'cyan', 'pink'])
ax3.set_title("Bar Plot: Random Values")
ax3.set_xlabel("Categories")
ax3.set_ylabel("Values")

# Subplot 4: Histogram
ax4 = fig.add_subplot(gs[1, 0])
data = np.random.randn(1000)
ax4.hist(data, bins=30, color='skyblue', edgecolor='black')
ax4.set_title("Histogram: Normal Distribution")
ax4.set_xlabel("Value")
ax4.set_ylabel("Frequency")

# Subplot 5: Boxplot using Seaborn
ax5 = fig.add_subplot(gs[1, 1])
sns.boxplot(data=[np.random.randn(100) for _ in range(4)], ax=ax5)
ax5.set_title("Boxplot: Random Data Groups")
ax5.set_xlabel("Groups")
ax5.set_ylabel("Values")

# Subplot 6: Heatmap using Seaborn
ax6 = fig.add_subplot(gs[1, 2])
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', ax=ax6)
ax6.set_title("Heatmap: Random Data")

# Adjust and show plot
plt.suptitle("Big Multi-Plot Visualization in Python", fontsize=18, fontweight='bold')
plt.show()
