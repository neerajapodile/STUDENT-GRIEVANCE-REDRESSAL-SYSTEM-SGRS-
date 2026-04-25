

students = []

def add_student():
    sid = input("Enter Student ID : ")
    name = input("Enter Student Name : ")
    dept = input("Enter Department : ")

    record = {
        "ID": sid,
        "Name": name,
        "Department": dept
    }

    students.append(record)

    print("Student Added Successfully")


def view_students():
    print("\nSTUDENT RECORDS")

    for s in students:
        print(s)


def search_student():
    sid = input("Enter ID to Search : ")

    for s in students:
        if s["ID"] == sid:
            print("Record Found")
            print(s)
            return

    print("Student Not Found")


# ---------------- grievance.py ----------------

grievances = []

def add_grievance():
    gid = "G" + str(len(grievances) + 1)

    sid = input("Enter Student ID : ")
    category = input("Enter Category : ")
    issue = input("Enter Issue : ")

    record = {
        "Grievance_ID": gid,
        "Student_ID": sid,
        "Category": category,
        "Issue": issue,
        "Status": "Pending"
    }

    grievances.append(record)

    print("Grievance Submitted")
    print("Generated ID :", gid)


def view_grievances():
    print("\nALL GRIEVANCES")

    for g in grievances:
        print(g)


# ---------------- admin.py ----------------

from grievance import grievances

def update_status():
    gid = input("Enter Grievance ID : ")

    for g in grievances:
        if g["Grievance_ID"] == gid:
            status = input("Enter New Status : ")
            g["Status"] = status
            print("Status Updated")
            return

    print("Grievance Not Found")


# ---------------- reports.py ----------------

from grievance import grievances

def pending_report():
    print("\nPENDING GRIEVANCES")

    for g in grievances:
        if g["Status"] == "Pending":
            print(g)


def resolved_report():
    print("\nRESOLVED GRIEVANCES")

    for g in grievances:
        if g["Status"] == "Resolved":
            print(g)


# ---------------- main.py ----------------

from student import add_student, view_students, search_student
from grievance import add_grievance, view_grievances
from admin import update_status
from reports import pending_report, resolved_report

while True:

    print("\n====== STUDENT GRIEVANCE SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Grievance")
    print("5. View Grievances")
    print("6. Update Status")
    print("7. Pending Report")
    print("8. Resolved Report")
    print("9. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        add_grievance()

    elif choice == "5":
        view_grievances()

    elif choice == "6":
        update_status()

    elif choice == "7":
        pending_report()

    elif choice == "8":
        resolved_report()

    elif choice == "9":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
```
