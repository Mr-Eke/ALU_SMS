#!/usr/bin/python3
"""
This module defines the GradeManagement class to handle the grading
system within the school management system.
"""


class Student:
    def __init__(self, student_id, full_name, intake, trimester):
        self.student_id = student_id
        self.full_name = full_name
        self.intake = intake
        self.trimester = trimester
        self.grades = {}

class Assignment:
    def __init__(self, name, assig_type, score, weight):
        self.name = name
        self.assig_type = assig_type
        self.score = score
        self.weight = weight

    def get_weighted_score(self):
        return (self.score / 100) * self.weight
class GradeManagement:
    def __init__(self, enrolled_student):
        """
        Initialize with an instance of StudentEnrollment to access enrolled students.
        Args:
            enrolled_student (StudentEnrollment): An instance of StudentEnrollment
            for managing students.
        """
        self.enrolled_student = enrolled_student

    def add_grade(self):
        """ This method adds grade for a specific student and module."""

        student_id = int(input("Enter Student ID: "))
        if student_id in self.enrolled_student.students:
            student = self.enrolled_student.students[student_id]
            module = input("Enter module name: ")
            try:
                grade = float(input("Enter grade for module (0-100): "))
                if 0 <= grade <= 100:
                    student.grades[module] = grade
                    print(f"\n---- Grade added for {module}. ----")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        else:
            print("Student ID not found.")

    def view_grades(self):
        """
        View all grades for a specific student by their ID.
        """
        student_id = int(input("Enter Student ID to view grades: "))
        if student_id in self.enrolled_student.students:
            student = self.enrolled_student.students[student_id]
            if student.grades:
                print(f"\nGrades for {student.full_name}:")
                for module, grade in student.grades.items():
                    print(f"{module}: {grade}")
            else:
                print("No grades available for this student.")
        else:
            print("Student ID not found.")

