import csv

from student import Student

LOG_FILE_PATH = 'file_handling/logs.txt'
INPUT_FILE_PATH = 'file_handling/input.csv'

# This script reads student data from a CSV file, processes it, and logs any errors encountered during the import.
def import_students_from_file(input_file_path, log_file_path):
    students = []
    
    with open(input_file_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            try:
                if row:  # Check if the row is not empty
                    name = row[0].strip('"')
                    age = int(row[1].strip('"'))
                    score = int(row[2].strip('"'))
                    students.append(Student(name, age, score))
            except ValueError:
                print(f"Skipping invalid row: {row}")
                with open(log_file_path, mode='a') as log_file:
                    log_file.write(f"Skipping invalid row: {row}\n")
    return students

def store_valid_student(student, log_file_path):
    try:
        with open(log_file_path, mode='a') as log_file:
            log_file.write(f"Valid student: {student}\n")
    except Exception as e:  
        print(f"Error logging valid student: {e}")

def store_invalid_student(student, log_file_path):
    try:
        with open(log_file_path, mode='a') as log_file:
            log_file.write(f"Invalid student: {student}\n")
    except Exception as e:
        print(f"Error logging invalid student: {e}")

def log_error(message, log_file_path):
    try:
        with open(log_file_path, mode='a') as log_file:
            log_file.write(f"Error: {message}\n")
    except Exception as e:
        print(f"Error logging message: {e}")

# Main function to execute the import and handle exceptions
def main():
    try:
        imported_students = import_students_from_file(INPUT_FILE_PATH, LOG_FILE_PATH)
        for student in imported_students:
            if student.is_valid():
                store_valid_student(student, LOG_FILE_PATH)
            else:
                store_invalid_student(student, LOG_FILE_PATH)
    except FileNotFoundError as e:
        message = f"File not found: {e}"
        print(message)
        log_error(message, LOG_FILE_PATH)
    except Exception as e:
        message = "An unexpected error occurred: {e}"
        print(message)
        log_error(message, LOG_FILE_PATH)
        

if __name__ == "__main__":
    main()

