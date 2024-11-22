#!/usr/bin/python3
import json
from student import Student
from assignment import Assignment
from assignment import load_data, save_data

# Data files for storage
STUDENTS_FILE = "students.json"
ASSIGNMENTS_FILE = "assignments.json"

class SchoolManagementSystem:
    def __init__(self):
        pass

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
        print(f"Student {full_name} enrolled with ID {student_id}.")
        self.save_students()
