# square = lambda x: x**2
# print(f"square(2): {square(2)}")
# print(f"square(3): {square(3)}")
# print(f"square(4): {square(4)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_squared = list(map(lambda x: x**2, numbers))
print(f"numbers_squared: {numbers_squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"evens: {evens}")

squares_of_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"squares_of_evens: {squares_of_evens}")

students = [
    {"name": "John", "age": 20, "grade": 85},
    {"name": "Jane", "age": 21, "grade": 90},
    {"name": "Jim", "age": 22, "grade": 78},
    {"name": "Jill", "age": 23, "grade": 88},
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True) 
print(f"sorted_students: {sorted_students}")








