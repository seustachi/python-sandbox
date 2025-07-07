name = "Sama"


if name == "Sam":
    print ("Hello Sam!")
else:
    print ("What's your name?")


print("Hello, %s!" % name)

print("Hello, {}!".format(name))
def greet(name):
    return f"Hello, {name}!"

print(greet(name))

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"Number: {number}")

def add(a, b):
    return a + b

result = add(5, 10)
print(f"Result of addition: {result}")

numbers.insert(2, 60)
print(numbers)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "jobs":
    [
        {
            "title": "Engineer",
            "company": "TechCorp"
        },
        {
            "title": "Designer",
            "company": "Creative Inc."
        }
    ]
}

print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

size = person.get("size", "Not specified")
# size = person["size"] BOOM
print(f"Size: {size}")

def print_jobs(jobs):
    for job in jobs:
        print(f"Title: {job['title']}, Company: {job['company']}")

print_jobs(person["jobs"])  

set_of_numbers = list(range(1, 11))
print(f"Set of numbers: {set_of_numbers}")

numbers = [1, 2, 3, 4, 5]
numbers_as_set = {1, 2, 3, 4, 5}
numbers_as_tuple = (1, 2, 3, 4, 5)
print(f"List: {numbers}, Set: {numbers_as_set}, Tuple: {numbers_as_tuple}")

x, y, z, *rest = numbers_as_tuple
print(f"x: {x}, y: {y}, z: {z}, rest: {rest}")

def doManythingsAndCoffee(*args):

    """
    This function does many things and coffee.

    It takes any number of arguments, and returns a tuple of two values.
    The first value is the sum of all the arguments, and the second value
    is their average.

    Parameters
    ----------
    *args : int
        Any number of integers

    Returns
    -------
    tuple
        (sum of all arguments, average of all arguments)
    """

    def average(args):
        return sum(args) / len(args) if args else 0

    return sum(args), average(args), max(args), min(args)

sum, average, max, min = doManythingsAndCoffee(1, 2, 3, 4, 5)
print(f"Sum: {sum}, Average: {average}, Max: {max}, Min: {min}")