
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)
    def check_result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")
# Creating Objects
student1 = Student("Mohsin", 85)
student2 = Student("Ali", 40)
# Calling Functions
student1.show_details()
student1.check_result()
1
print("----------------")
student2.show_details()
student2.check_result()
