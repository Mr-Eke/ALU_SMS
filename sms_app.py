#!/usr/bin/python3
import sys
from student import Student
from enrollment import StudentEnrollment

new_student = StudentEnrollment()

while True:
    print("\n-----------------------------------------")
    print("\tSCHOOL MANAGEMENT SYSTEM")
    print("-----------------------------------------\n")

    print("1. Student Enrollment")
    print("2. Manage Student Records")
    print("3. Student Grade Input")
    print("4. CGPA Calculation")
    print("5. View Student Grades")
    print("6. Exit\n\n-----------------------------------------")

    selected_menu = int(input("Choose a menu: "))

    if selected_menu == 1:
        new_student.enroll_student()

    if selected_menu == 6:
        sys.exit()

