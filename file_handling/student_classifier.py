import csv
import json
import os

from student import Student

LOG_FILE_PATH = 'staging/logs.txt'
INPUT_FILE_PATH = 'staging/input.csv'
VALID_STUDENTS_FILE_PATH = 'staging/valid.json'
INVALID_STUDENTS_FILE_PATH = 'staging/invalid.json'

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



def store_student(student, file_path):
    data = []  # ✅ Initialize with empty array

    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON file must contain an array")
        
        data.append(student.__dict__)

        with open(file_path, mode='w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:  
        message = f"Error logging student: {e}"
        log_error(message, LOG_FILE_PATH)



def log_error(message, log_file_path):
    try:
        with open(log_file_path, mode='a') as log_file:
            log_file.write(f"Error: {message}\n")
            print(f"Error logged: {message}")
    except Exception as e:
        print(f"Error logging message: {e}")

# Main function to execute the import and handle exceptions
def main():
    try:
        imported_students = import_students_from_file(INPUT_FILE_PATH, LOG_FILE_PATH)
        for student in imported_students:
            if student.is_valid():
                store_student(student, VALID_STUDENTS_FILE_PATH)
            else:
                store_student(student, INVALID_STUDENTS_FILE_PATH)
    except FileNotFoundError as e:
        message = f"File not found: {e}"
        log_error(message, LOG_FILE_PATH)
    except Exception as e:
        message = f"An unexpected error occurred: {e}"
        log_error(message, LOG_FILE_PATH)
        

if __name__ == "__main__":
    main()

