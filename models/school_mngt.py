#!/usr/bin/python3
""" School Management System.
Provides a basic management system for students and their assignments.
It uses JSON files to persist data and includes functionality for
enrolling students annd adding assignments to their records."""

import json
from models.student import Student
from models.assignment import Assignment, load_data, save_data

# Path to file data storage
STUDENTS_FILE = "students.json"

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


    def save_students(self):
        """ Saves the current student data to the students JSON file.
        """
        # Convert Student objects to dictionary format for JSON serialization
        student_data = {key: val.to_dict() for key, val in self.students.items()}
        save_data(student_data, STUDENTS_FILE)


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
            assignment details."""
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

        total_FA , total_FA_weight, total_SA, total_SA_weight = 0, 0, 0, 0

        # Iterate through the student's grades to calculate totals
        for grade in student.grades.values():
            weighted_score = grade["weighted_score"]  # Retrieve Assignmnt weighted score
            if grade["type"] == "Formative":
                total_FA_weight += grade["weight"]
                if total_FA_weight <= 60:
                    total_FA += weighted_score
            elif grade["type"] == "Summative":
                total_SA_weight += grade["weight"]
                if total_SA_weight <= 40:
                    total_SA += weighted_score

        # Overall score (can be final grade)
        self.total_score = total_FA + total_SA

        # Display the student's final grade and status
        print("--" * 21)
        print(f"\nTotal FA Score is {round(total_FA, 2)}%" + (" and it's below 30%" if total_FA < 30 else ''))
        print(f"Total SA Score is {round(total_SA, 2)}%" + (" and it's below 20%" if total_SA < 20 else ''))
        print(f"\nFinal Grade for {student.full_name}: {self.total_score:.2f}%")

        # Determine course progression
        if self.total_score < 50 or total_FA < 30 or total_SA < 20:
            print("=== Failed and must retake the course ===")
        else:
            print("=== Congrats, Passed and have Progressed ===.")

        # Generate transcript in users prefered order
        transcript = input("\nPrint transcript? (asc/dsc) or 'no' to return to menu: ").lower()
        if transcript == "asc":
            print("\nTranscript Breakdown (Ascending order):")
            self.create_transcript(student_id, asc=True)
        elif transcript == "dsc":
            print("\nTranscript Breakdown (Descending order):")
            self.create_transcript(student_id, asc=False)
        else:
            return


    def get_cgpa(self, stud_id):
        if stud_id not in self.students:
            print("Student ID not found.")
            return

        stud = self.students[stud_id]

        # Calculate total weighted scores
        totals = sum(grade["weighted_score"] for grade in stud.grades.values())
        cgpa = (totals / 100) * 5
        cgpa_ = f"CGPA for {stud.full_name}: {cgpa:.2f}/5"

        print("\n" + len(cgpa_) * "=")
        print(cgpa_)
        print(len(cgpa_) * "=")


    def create_transcript(self, student_id, asc=True):
        """ Generates a transcript of all assignments for a specific student,
        sorted by score.
        Args:
            student_id (int): ID of the student whose transcript is to be created.
            asc (bool): If True, sorts by ascending order; otherwise, descending.
        """
        if student_id not in self.students:
            print("Student ID not found.")
            return

        # Retrieve the student's assignment grades
        student = self.students[student_id]
        if not student.grades:
            print(f"No assignments found for {student.full_name}.")
            return

        def get_score(assignment_item):
            """Return the score of an assignment for sorting."""
            return assignment_item[1]["score"]

        # Sort assignments based on score
        sorted_assignments = sorted(
            student.grades.items(),
            key=get_score,
            reverse=not asc,
        )

        # Print the transcript in tabular format
        fields = f"{'Assignment'.ljust(23)}{'Type'.ljust(13)}{'Score(%)'.ljust(10)}{'Weight(%)'.ljust(10)}{'Weighted Score'.ljust(15)}"
        print("-" * len(fields))
        print(fields)
        print("-" * len(fields))
        for name, details in sorted_assignments:
            name = name.ljust(23)
            assig_type = details["type"].ljust(13)
            score = f"{details['score']:.2f}".ljust(10)
            weight = f"{details['weight']:.2f}".ljust(10)
            weighted_score = f"{details['weighted_score']:.2f}".ljust(15)
            print(f"{name}{assig_type}{score}{weight}{weighted_score}")
        print("-" * len(fields))
        print(f"Total: {round(self.total_score, 2)}%".rjust(61))


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
            print("\n" + "\tList of all enrolled students:")
            print(tabulate(table_data, headers=headers, tablefmt="pretty"))

        except FileNotFoundError:
            print("No data found. Please enroll a student first.")
