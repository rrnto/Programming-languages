# 1. Create a basic scatter plot
import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4]
y = [2, 3, 5, 7]

# Create the scatter plot
plt.scatter(x, y)

# Label the axes
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Title for the plot
plt.title('Basic Scatter Plot')

# Show the plot
plt.show()


# 2. Modify the scatter plot to include a line and use different marker colors

# Data points
x = [1, 2, 3, 4]
y = [2, 3, 5, 7]

# Create the scatter plot with different colors for the markers
plt.scatter(x, y, color='red', label='Data points')

# Plot a line connecting the points
plt.plot(x, y, color='blue', label='Connecting line')

# Label the axes
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Title for the plot
plt.title('Scatter Plot with Line')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# 3. Create a histogram of random data from a normal distribution

import numpy as np

# Generate 1000 data points from a normal distribution
data = np.random.normal(0, 1, 1000)

# Create a histogram
plt.hist(data, bins=30, edgecolor='black')

# Title and labels
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()


# 4. Create a bar chart for the brightness of five stars

# Data for stars and brightness
stars = ['Sirius', 'Canopus', 'Arcturus', 'Alpha Centauri', 'Vega']
brightness = [1.46, -0.72, -0.05, 0.01, 0.03]
colors = ['yellow', 'gray', 'orange', 'red', 'blue']

# Create a bar chart
plt.bar(stars, brightness, color=colors)

# Title and labels
plt.title('Brightness of Stars')
plt.xlabel('Stars')
plt.ylabel('Brightness')

# Add a legend
plt.legend(stars, title='Stars')

# Show the plot
plt.show()
