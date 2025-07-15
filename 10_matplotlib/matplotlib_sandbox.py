import matplotlib.pyplot as plt
import numpy as np

#x = [1, 2, 3, 4]
#y = [10, 20, 25, 30]


x = np.linspace(0, 10, 100)

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), 'b', label='sin(x)')
plt.plot(x, np.cos(x), 'r--', label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('sin(x) function')
plt.legend()



plt.show()

plt.subplot(2, 2, 2)
np.random.seed(42)
x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [1, 4, 9, 16, 25]

plt.scatter(x_scatter, y_scatter, alpha=0.6)
plt.title('Scatter plot')

plt.show()

#let's draw a bar plot

plt.subplot(2, 2, 3)
plt.bar(['A', 'B', 'C', 'D', 'E'], [1,4,9,16,25], color=['skyblue', 'lightcoral', 'lightgreen', 'lightyellow', 'lightpink'], alpha=0.6)
plt.title('Bar plot')
plt.show()







