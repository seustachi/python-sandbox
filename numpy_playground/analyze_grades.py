import numpy as np
from numpy.ma import mask_cols

students = np.array(["Alice", "Bob", "Charlie", "Sam", "Max"])

subjects = np.array(["Math", "Science", "English", "History"])

# Each student now has exactly 4 grades
students_grades = np.array([
    [83, 86, 89, 90],
    [78, 81, 85, 88],
    [90, 93, 95, 97],
    [70, 73, 75, 78],
    [80, 83, 85, 0]
])

average_per_student = np.average(students_grades, axis=1)
students_average = np.vstack((students, average_per_student))
print(f"Average per student: \n {students_average}")

average_per_subject = np.average(students_grades, axis=0)
print(f"Average per subject: \n {np.vstack((subjects, average_per_subject))}")

student_passes = average_per_student > 80

print(f"Students who passed: \n {students[student_passes]}")
print(f"Students who failed: \n {students[~student_passes]}")








