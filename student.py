#!/usr/bin/python3
import random
"""
This module defines the Student class used for managing student
information in a school management system.
"""


class Student:
    """
    A class to represent a student

    Attributes:
        student_id (int): The unique identifier for the student.
        full_name (str): The full name of the student.
        intake (str): The intake year or term for the student.
        trimester (str): Student trimester in the current academic year.
    """

    def __init__(self, student_id, full_name, intake, trimester):
        """Initializes a new Student instance with the above attributes."""

        self.grades = {}
        self.student_id = student_id
        self.full_name = full_name
        self.intake = intake
        self.trimester = trimester

    @staticmethod
    def generate_id():
        return random.randint(1000, 9999)

    def __str__(self):
        """
        Returns a string representation of the student's information.
        Returns:
            str: A formatted string containing the student's ID, name,
            intake, and trimester.
        """
        return (
            f"ID: {self.student_id}, Name: {self.full_name}, "
            f"Intake: {self.intake}, Trimester: {self.trimester}"
        )

