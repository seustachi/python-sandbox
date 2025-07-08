class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.__name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 60
    
    def is_valid(self):
        return isinstance(self.__name, str) and isinstance(self.age, int) and isinstance(self.grade, (int, float)) and self.age > 0 and self.grade >= 0 and self.grade <= 100
    
    @property 
    def name(self):
        return self.__name
    
# Example usage
if __name__ == "__main__":
    student1 = Student("Alice", 20, 85)
    student2 = Student("Bob", 19, 55)

    print(student1.get_info())
    print(f"Is {student1.name} passing? {'Yes' if student1.is_passing() else 'No'}")

    print(student2.get_info())
    print(f"Is {student2.name} passing? {'Yes' if student2.is_passing() else 'No'}")