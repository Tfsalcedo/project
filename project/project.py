import matplotlib.pyplot as plt

# sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# the line chart
plt.plot(x, y, marker='o', color='blue', label='Values')

# title and labels
plt.title('Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)

# show the plot
plt.show()