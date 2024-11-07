#!/usr/bin/python3
import random

class Student:
    def __init__(self, student_id, full_name, intake, trimester):
        self.student_id = student_id
        self.full_name = full_name
        self.intake = intake
        self.trimester = trimester

    def __str__(self):
        return (
            f"ID: {self.student_id}, Name: {self.full_name}, "
            f"Intake: {self.intake}, Trimester {self.trimester}"
        )
