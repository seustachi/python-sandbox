import csv
import json
import os
import logging

from student import Student

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Logging setup
LOG_FILE_PATH = os.path.join(BASE_DIR, 'staging', 'logs.txt')
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

INPUT_FILE_PATH = os.path.join(BASE_DIR, 'staging', 'input.csv')
VALID_STUDENTS_FILE_PATH = os.path.join(BASE_DIR, 'staging', 'valid.json')
INVALID_STUDENTS_FILE_PATH = os.path.join(BASE_DIR, 'staging', 'invalid.json')

# This script reads student data from a CSV file, processes it, and logs any errors encountered during the import.
def import_students_from_file(input_file_path):
    students = []
    try:
        with open(input_file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                try:
                    if row:  # Check if the row is not empty
                        name = row[0].strip('"')
                        age = int(row[1].strip('"'))
                        score = int(row[2].strip('"'))
                        students.append(Student(name, age, score))
                except (ValueError, IndexError) as e:
                    logging.warning(f"Skipping invalid row {row}: {e}")
    except FileNotFoundError as e:
        logging.error(f"Input file not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error reading input file: {e}", exc_info=True)
        raise
    return students


def store_student(student, file_path):
    data = []
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    logging.error(f"JSON decode error in {file_path}: {e}")
                    data = []  # Start fresh if file is corrupted
            if not isinstance(data, list):
                raise ValueError("JSON file must contain an array")
        data.append(student.__dict__)
        with open(file_path, mode='w') as file:
            json.dump(data, file, indent=2)
        logging.info(f"Stored student {student.__dict__} in {file_path}")
    except Exception as e:
        logging.error(f"Error storing student {student.__dict__} in {file_path}: {e}", exc_info=True)


def main():
    # Empty the log, valid, and invalid files before starting
    for path in [LOG_FILE_PATH, VALID_STUDENTS_FILE_PATH, INVALID_STUDENTS_FILE_PATH]:
        try:
            with open(path, 'w') as f:
                if path.endswith('.json'):
                    f.write('[]')  # Initialize JSON files as empty arrays
                else:
                    pass  # Just truncate log file
        except Exception as e:
            logging.error(f"Failed to clear file {path}: {e}", exc_info=True)
    try:
        imported_students = import_students_from_file(INPUT_FILE_PATH)
        for student in imported_students:
            try:
                if student.is_valid():
                    store_student(student, VALID_STUDENTS_FILE_PATH)
                else:
                    logging.info(f"Invalid student data: {student.__dict__}")
                    store_student(student, INVALID_STUDENTS_FILE_PATH)
            except Exception as e:
                logging.error(f"Error processing student {student.__dict__}: {e}", exc_info=True)
    except Exception as e:
        logging.critical(f"Critical error in main: {e}", exc_info=True)

if __name__ == "__main__":
    main()

