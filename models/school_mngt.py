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

        x = f"{full_name} with ID: {student_id} is successfully enrolled"
        print("\n" + len(x) * "=")
        print(x)
        print(len(x) * "=")
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
        print("\n" + len(added_assign) * '-')
        print(added_assign)
        print(len(added_assign) * '-')
        self.save_students()  # Save updated student data

    def calculate_overall_score(self, student_id):
        """ Calculates and displays the overall score for a student based on
            their assignments.

        Considers Formative (FA) and Summative (SA) assignment types,
        ensuring their respective weight limits are adhered to:
        - Formative assignments can have a total weight of up to 60.
        - Summative assignments can have a total weight of up to 40.
        Args:
            student_id (int): Student ID whose overall score is being calculated.
        """
        if student_id not in self.students:
            print("Student ID not found.")
            return

        # Retrieve the student object
        student = self.students[student_id]

        total_FA = 0
        total_FA_weight = 0
        total_SA = 0
        total_SA_weight = 0

        # Iterate through the student's grades to calculate totals
        for grade in student.grades.values():
            weighted_score = grade["weighted_score"]  # Retrieve Assign weighted score
            if grade["type"] == "Formative":
                total_FA_weight += grade["weight"]
                if total_FA_weight <= 60:
                    total_FA += weighted_score
            elif grade["type"] == "Summative":
                total_SA_weight += grade["weight"]
                if total_SA_weight <= 40:
                    total_SA += weighted_score

        # Overall score (can be final grade)
        total_score = total_FA + total_SA

        # Display the student's final grade and status
        print(f"\nTotal FA Score: {round(total_FA, 2)}%" + (" and it's below 30%" if total_FA < 30 else ''))
        SA = f"Total SA Score: {round(total_SA, 2)}%" + (" and it's below 20%" if total_SA < 20 else '')
        print(SA + "\n" + "-" * len(SA))
        print(f"\nFinal Grade for {student.full_name}: {total_score:.2f}%")

        # Determine course progression
        if total_score < 50 or total_FA < 30 or total_SA < 20:
            print("=== Failed and must retake the course ===")
        else:
            print("=== Congrats, Passed and have Progressed ===.")

    def view_student_records(self):
        """ Displays all enrolled student records in a tabular format.

        Reads student data from the JSON file and organizes it into a table
        with columns for ID, Name, Trimester, and Intake. """
        try:
            # Open and load student data from the JSON file
            with open(STUDENTS_FILE, "r") as file:
                students = json.load(file)
            if not students: # Empty Dict
                print("No students enrolled yet.")
                return

            # Prepare data for display in a tabular format
            table_data = []

            for student_id, student_info in students.items():
                table_data.append([
                    student_id,
                    student_info["full_name"],
                    student_info["trimester"],
                    student_info["intake"],
                ])

            headers = ["ID", "Name", "Trimester", "Intake"]

            # Print the table using the tabulate library
            from tabulate import tabulate

            print("\n" + "\tList of all the enrolled students:")
            print(tabulate(table_data, headers=headers, tablefmt="pretty"))
        except FileNotFoundError:
            print("No data found. Please enroll a student first.")

    def create_transcript(self, asc=True):
        """ Generates a transcript of all assignments sorted by score.
        Args:
            asc (bool): If True, sorts by asc order; otherwise, descending."""
        def score_to_sort(assignment):
            return assignment.score

        # Sort assignments based on the chosen order
        sorted_assignments = sorted(
            self.assignment_list, key=score_to_sort, reverse=not asc
        )

        fields = f"{'Assignment'.ljust(45)}{'Type'.ljust(15)}{'Score(%)'.ljust(10)}{'Weight(%)'.ljust(10)}"
        print(fields)
        print("-" * len(fields))
        for assignment in sorted_assignments:
            name = assignment.name.ljust(45)
            assig_type = assignment.assig_type.ljust(15)
            score = f"{assignment.score}".ljust(10)
            weight = f"{assignment.weight}".ljust(10)
            print(f"{name}{assig_type}{score}{weight}")
        print("-" * len(fields))
