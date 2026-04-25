class Student:

    def __init__(self, name, sid, dept, issue):
        self.name = name
        self.sid = sid
        self.dept = dept
        self.issue = issue

    def display(self):
        print("\nStudent Name :", self.name)
        print("Student ID   :", self.sid)
        print("Department   :", self.dept)
        print("Issue        :", self.issue)

    def update_issue(self, new_issue):
        self.issue = new_issue
        print("Issue Updated")

s1 = Student("Lucky", "101", "CSE", "Exam Marks")

s1.display()

s1.update_issue("Fee Issue")

s1.display()
