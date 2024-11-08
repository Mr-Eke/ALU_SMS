#!/usr/bin/python3
from student import Student


class StudentEnrollment:

    def __init__(self):
        self.students = {}

    def enroll_student(self):
        # try:
        full_name = input("\nEnter first and last name seperated with space: ")
        fs_name, ls_name = full_name.split(" ")
    # except ValueError:
        intake = input("Enter your intake (e.g 2024M for May 2024 intake): ")
        trimester = input("Enter your trimester (e.g T2 for trimester 2): ")
        id = Student.generate_id()

        self.students[id] = Student(id, full_name, intake, trimester)
        print("\n==================================================")
        print(f"{fs_name} with ID: {id} is successfully enrolled!")
        print("==================================================")
