'''
Mini Project: Student Marks Analyzer
📘 Problem Statement:
Build a class-based system to store student marks, compute statistics (average, max, min), and use NumPy arrays for high-performance computation.
'''

import numpy as np

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = np.array(marks)  # NumPy array from Day 1

    def display(self):
        print(f"\nStudent: {self.name}")
        print("Marks:", self.marks)

    def get_average(self):
        return np.mean(self.marks)

    def get_highest(self):
        return np.max(self.marks)

    def get_lowest(self):
        return np.min(self.marks)


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student_obj):
        self.students.append(student_obj)

    def show_all(self):
        for student in self.students:
            student.display()
            print(f"Average: {student.get_average():.2f}")
            print(f"Highest: {student.get_highest()}")
            print(f"Lowest: {student.get_lowest()}\n")

    def class_average(self):
        all_marks = np.concatenate([s.marks for s in self.students])
        return np.mean(all_marks)


# ---------- Usage ----------
if __name__ == "__main__":
    s1 = Student("Alice", [85, 92, 78, 90])
    s2 = Student("Bob", np.arange(70, 90, 5))  # NumPy use from Day 1
    s3 = Student("Charlie", np.ones(5) * 80)

    classroom = Classroom()
    classroom.add_student(s1)
    classroom.add_student(s2)
    classroom.add_student(s3)

    classroom.show_all()
    print("Class Average:", classroom.class_average())
