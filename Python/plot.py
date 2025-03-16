import matplotlib.pyplot as plt
import numpy as np

# Line Plot
y = np.array([3, 8, 1, 10])
plt.figure(figsize=(10, 8))

plt.subplot(3, 2, 1)
plt.plot(y, 'o:r')
plt.title("Line Plot")

# Scatter Plot
x = np.array([1, 2, 3, 4])
plt.subplot(3, 2, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")

# Bar Plot
x_labels = np.array(["A", "B", "C", "D"])
plt.subplot(3, 2, 3)
plt.bar(x_labels, y)
plt.title("Bar Plot")

# Histogram
x_hist = np.random.normal(0, 1, 1000)
plt.subplot(3, 2, 4)
plt.hist(x_hist, bins=30)
plt.title("Histogram")

# Pie Chart
labels = ["A", "B", "C", "D"]
sizes = [3, 8, 1, 10]
plt.subplot(3, 2, 5)
plt.pie(sizes, labels=labels)
plt.title("Pie Chart")

# Box Plot
data = np.random.normal(0, 1, 100)
plt.subplot(3, 2, 6)
plt.boxplot(data)
plt.title("Box Plot")

plt.tight_layout()
plt.show()