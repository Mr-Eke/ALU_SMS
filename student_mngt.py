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
