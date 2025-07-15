import time
import numpy as np

# 1. Creating Arrays
# a. From Python Lists
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)
print(python_list)
print(numpy_array)

# b. From Range
numpy_array_from_range = np.arange(10)
print(numpy_array_from_range)

"""
large_list = list(range(100000000))
numpy_array_from_large_list = np.array(large_list)
#print(large_list)
print(numpy_array_from_large_list)

 start_time = time.time()
result_list = [x**3 for x in large_list]
end_time = time.time()
print(f"Time taken for list comprehension: {end_time - start_time} seconds")

start_time = time.time()
result_numpy = numpy_array_from_large_list**3
end_time = time.time()
print(f"Time taken for numpy array: {end_time - start_time} seconds") """

# c. From Random
numpy_array_from_random = np.random.rand(10)
print(numpy_array_from_random)

# d. From Zeros
zeros = np.zeros(10)
ones = np.ones(10)
range_array = np.arange(10)
linspace_array = np.linspace(0, 10, 11)
print(linspace_array)

random_array = np.random.randint(10, 100, (10, 10))
print(random_array)

