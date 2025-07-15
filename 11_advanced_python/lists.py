numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x**2 for x in numbers]
print(squares)

evens = [x for x in numbers if x % 2 == 0]
print(evens)

matrix = [[i*j for j in range(1, 5)] for i in range(1, 4)]
print(matrix)

fruits = ['apple', 'banana', 'cherry', 'date' ,'banana']

word_lengths_list = [len(word) for word in fruits]
print(f"word_lengths_list: {word_lengths_list}")

word_lengths_dict = {word: len(word) for word in fruits}
print(f"word_lengths_dict: {word_lengths_dict}")

unique_lengths_set = {len(word) for word in fruits}
print(f"unique_lengths_set: {unique_lengths_set}")

squares_generator = (x**2 for x in range(1, 100000000000))
print(f"squares_generator: {squares_generator}")
print(f"next(squares_generator): {next(squares_generator)}")
print(f"next(squares_generator): {next(squares_generator)}")
print(f"next(squares_generator): {next(squares_generator)}")

square = lambda x: x**2
print(f"square(2): {square(2)}")
print(f"square(3): {square(3)}")
print(f"square(4): {square(4)}")





