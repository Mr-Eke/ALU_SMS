#!/usr/bin/python3
import json
from models.student import Student
from models.assignment import Assignment
from models.assignment import load_data, save_data

# Data files for storage
STUDENTS_FILE = "students.json"
ASSIGNMENTS_FILE = "assignments.json"

class SchoolManagementSystem:
    def __init__(self):
        student_data = load_data(STUDENTS_FILE)
        self.students = {}

    # Iterate over each student in the loaded data and convert to Student objects
        for k, v in student_data.items():
            student_id = int(k)
            student = Student.from_dict(v)
            self.students[student_id] = student

        # Load assignment data from the file
        self.assignments = load_data(ASSIGNMENTS_FILE)

    def save_students(self):
        student_data = {}
        for k, v in self.students.items():
            student_data[k] = v.to_dict()
        save_data(student_data, STUDENTS_FILE)

    def save_assignments(self):
        save_data(self.assignments, ASSIGNMENTS_FILE)

    def enroll_student(self):
        full_name = input("\nEnter full name: ")
        intake = input("Enter intake (e.g., 2024M): ")
        trimester = input("Enter trimester (e.g., T2): ")
        student_id = len(self.students) + 1  # Simple ID generator
        student = Student(student_id, full_name, intake, trimester)
        self.students[student_id] = student
        print("\n==================================================")
        print(f"{full_name} with ID: {student_id} is successfully enrolled")
        print("==================================================")
        self.save_students()
