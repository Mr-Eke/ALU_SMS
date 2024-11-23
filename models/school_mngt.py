#!/usr/bin/python3
"""
School Management System

This script provides a basic management system for students and their assignments.
It uses JSON files to persist data and includes functionality for enrolling students
and adding assignments to their records.
"""

import json
from models.student import Student
from models.assignment import Assignment, load_data, save_data

# Constants for data file paths
STUDENTS_FILE = "students.json"
ASSIGNMENTS_FILE = "assignments.json"

class SchoolManagementSystem:
    """ A class to manage student enrollment and assignment tracking.
    Attributes:
        students (dict): A dictionary of Student objects keyed by student ID.
        assignments (dict): A dictionary containing assignment data.
    """

    def __init__(self):
        """ Initializes the SchoolManagementSystem by loading student and
        assignment data from their respective JSON files.
        """
        # Load student data and convert it to Student objects
        student_data = load_data(STUDENTS_FILE)
        self.students = {}
        for key, value in student_data.items():
            student_id = int(key)  # Convert ID from str to int
            student = Student.from_dict(value)  # Create Student object from dictionary
            self.students[student_id] = student

        # Load assignment data
        self.assignments = load_data(ASSIGNMENTS_FILE)

    def save_students(self):
        """ Saves the current student data to the students JSON file.
        """
        # Convert Student objects to dictionary format for JSON serialization
        student_data = {key: val.to_dict() for key, val in self.students.items()}
        save_data(student_data, STUDENTS_FILE)

    def save_assignments(self):
        """ Saves the current assignment data to the assignments JSON file.
        """
        save_data(self.assignments, ASSIGNMENTS_FILE)

    def enroll_student(self):
        """ Enrolls a new student into the system by collecting their details
            and assigning them an ID.
        """
        full_name = input("\nEnter first and last name separated by space: ")
        intake = input("Enter intake (e.g., 2024M for May, 2024 intake): ")
        trimester = input("Enter trimester (e.g., T2 for trimester 2): ")
        student_id = len(self.students) + 1  # Generate a new student ID
        student = Student(student_id, full_name, intake, trimester)
        self.students[student_id] = student
        print("\n==================================================")
        print(f"{full_name} with ID: {student_id} is successfully enrolled")
        print("==================================================")
        self.save_students()  # Save updated student data

    def add_assignment(self):
        """ Adds an assignment to a student's record by taking their ID and
            assignment details.
        """
        student_id = int(input("\nEnter student ID to add assignment: "))
        if student_id not in self.students:
            print("Student ID not found.")
            return

        # Collect assignment details
        name = input("Assignment Name: ")
        assig_type = input("Assignment Type (Formative (FA)/Summative (SA)): ").capitalize()
        score = float(input("Score (0-100): "))
        weight = float(input("Assignment Weight (1-40 for FA, and 1-60 for SA): "))

        # Create an Assignment object and calculate the weighted score
        assignment = Assignment(name, assig_type, score, weight)
        student = self.students[student_id]
        student.grades[name] = {
            "type": assig_type,
            "score": score,
            "weight": weight,
            "weighted_score": assignment.get_weighted_score()
        }

        # Display confirmation message
        added_assign = f"'{name}' assignment is added to {student.full_name}'s record."
        print()
        print(len(added_assign) * '-')
        print(added_assign)
        print(len(added_assign) * '-')
        self.save_students()  # Save updated student data
