#!/usr/bin/python3

from enrollment import StudentEnrollment

class ManageStudentsRecord:
    def __init__(self, enrolled_student):
        self.enrolled_student =  enrolled_student
    def view_students(self):

        for student_attr in self.enrolled_student.students.values():
            print(student_attr)
