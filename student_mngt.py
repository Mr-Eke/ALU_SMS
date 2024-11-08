#!/usr/bin/python3

from enrollment import StudentEnrollment

class ManageStudentsRecord:
    def __init__(self, enrolled_student):
        self.enrolled_student =  enrolled_student
    def view_students(self):

        print("\n===============================================================")
        print("\tList of Enrolled Students\n-----------------------------------------")
        for student_attr in self.enrolled_student.students.values():
            print(student_attr)
        print("===============================================================")

    def view_student_by_id(self):
        id_input = int(input("Enter student ID: "))
        for student_id, val in self.enrolled_student.students.items():
            if student_id == id_input:
                print(val)
            else:
                print("Theres no Student with such ID")

    def modify_student_record(self):
        """ Modify details of a specific student by their ID."""

        student_id = int(input("Enter Student ID: "))
        if student_id in self.enrolled_student.students:
            selected_student = self.enrolled_student.students[student_id]
            print(f"Current record: {selected_student}")

            print("Choose what to update:")
            print("[1] Name")
            print("[2] Trimester")
            print("[3] Intake")
            record_to_update = int(input("Enter your choice: "))

            if record_to_update == 1:
                new_name = input("Enter new name: ")
                selected_student.full_name = new_name
                print("Name updated successfully.")
            elif record_to_update == 2:
                new_trimester = input("Enter new trimester: ")
                selected_student.trimester = new_trimester
                print("Trimester updated successfully.")
            elif record_to_update == 3:
                new_intake = input("Enter new intake: ")
                selected_student.intake = new_intake
                print("Intake updated successfully.")
            else:
                print("Invalid choice.")
        else:
            print("Student ID not found.")

