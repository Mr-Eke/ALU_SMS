#!/usr/bin/python3

from student import Student

class SchoolManagementSystem:
    def __init__(self):
        pass

    def enroll_student(self):
        full_name = input("\nEnter full name: ")
        intake = input("Enter intake (e.g., 2024M): ")
        trimester = input("Enter trimester (e.g., T2): ")
        student_id = len(self.students) + 1  # Simple ID generator
        student = Student(student_id, full_name, intake, trimester)
        self.students[student_id] = student
        print(f"Student {full_name} enrolled with ID {student_id}.")
        self.save_students()
