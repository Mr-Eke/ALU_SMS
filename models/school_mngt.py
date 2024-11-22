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

        # Iterate over each student to Student objects
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
        full_name = input("\nEnter first and last name seperated by space: ")
        intake = input("Enter intake (e.g., 2024M for May, 2024 intake): ")
        trimester = input("Enter trimester (e.g., T2 for trimester 2): ")
        student_id = len(self.students) + 1  # Simple ID generator
        student = Student(student_id, full_name, intake, trimester)
        self.students[student_id] = student
        print("\n==================================================")
        print(f"{full_name} with ID: {student_id} is successfully enrolled")
        print("==================================================")
        self.save_students()

    def add_assignment(self):
        student_id = int(input("\nEnter student ID to add assignment: "))
        if student_id not in self.students:
            print("Student ID not found.")
            return
        name = input("Assignment Name: ")
        assig_type = input("Assignment Type (Formative (FA)/Summative (SA)): ").capitalize()
        score = float(input("Score (0-100): "))
        weight = float(input("Assignment Weight (1-40 for FA, and 1-60 for SA): "))
        assignment = Assignment(name, assig_type, score, weight)
        student = self.students[student_id]
        student.grades[name] = {
            "type": assig_type,
            "score": score,
            "weight": weight,
            "weighted_score": assignment.get_weighted_score()
        }
        print(f"\n'{name}' assignment is added to {student.full_name}'s record.")
        self.save_students()
