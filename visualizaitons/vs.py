import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
x1 = [1, 2, 3, 4, 5]
y1 = [5, 4, 3, 2, 1]

plt.plot(x, y, label='x vs y', color='blue', marker='o')
plt.plot(x1, y1, label='x1 vs y1', color='red', marker='s')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot Example')
plt.legend()
plt.show()
