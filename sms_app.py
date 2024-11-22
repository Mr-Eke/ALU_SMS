#!/usr/bin/python3
import sys
from models.student import Student
from models.assignment import Assignment
from models.student_mngt import SchoolManagementSystem

def main():
    system_manager = SchoolManagementSystem()
    while True:
        print("\n\tSCHOOL MANAGEMENT SYSTEM")
        print("-----------------------------------------\n")
        print("1. Student Enrollment\n2. Add Assignment")
        print("3. Calculate Grade\n4. View Students")
        print("4. CGPA Calculation")
        print("5. Exit\n")
        choice = input("Choose an option: ")
        if choice == "1":
            system_manager.enroll_student()
        elif choice == "2":
            system_manager.add_assignment()
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            system_manager.calculate_overall_score(student_id)
        elif choice == "4":
            system_manager.view_student_records()
        elif choice == "5":
            exit_option = input("are you sure you want to exit (yes/no): ").lower()
            sys.exit() if exit_option == "yes" else ""
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
