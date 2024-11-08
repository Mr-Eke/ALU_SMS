#!/usr/bin/python3
import sys
from student import Student
from grades_mngt import GradeManagement
from enrollment import StudentEnrollment
from student_mngt import ManageStudentsRecord

new_student = StudentEnrollment()
grade_student = GradeManagement(new_student)
mange_students = ManageStudentsRecord(new_student)

while True:
    print("\n\tSCHOOL MANAGEMENT SYSTEM")
    print("-----------------------------------------\n")

    print("1. Student Enrollment")
    print("2. Manage Student Records")
    print("3. Grade Management")
    print("4. CGPA Calculation")
    print("5. View Student Grades")
    print("6. Exit\n")

    selected_menu = int(input("Choose a menu: "))

    if selected_menu == 1:
        new_student.enroll_student()
    elif selected_menu == 2:
        print(("[1] View a specific Student "
       "[2] View all Students "
       "[3] Modify a Student"))
        option_selected = int(input("Choose your option (1, 2 or 3): "))
        if option_selected == 1:
            mange_students.view_student_by_id()
        elif option_selected == 2:
            mange_students.view_students()
        elif option_selected == 3:
            mange_students.modify_student_record()
    elif selected_menu == 3:
        grade_option = int(input("Enter 1 to add grades or 2 to view grades: "))
        if grade_option == 1:
            grade_student.add_grade()

    if selected_menu == 6:
        exit_option = input("are you sure you want to exit (yes/no): ").lower()
        sys.exit() if exit_option == "yes" else ""

