# WEEK 9
# Full Student Grievance Redressal System

from datetime import datetime

students = []
grievances = []

# ---------------- STUDENT MODULE ----------------

def add_student():
    print("\nADD STUDENT")
    sid = input("Enter Student ID : ")
    name = input("Enter Name : ")
    dept = input("Enter Department : ")

    student = {
        "ID": sid,
        "Name": name,
        "Department": dept
    }

    students.append(student)
    print("Student Added Successfully")


def view_students():
    print("\nALL STUDENTS")
    for s in students:
        print(s)


# ---------------- GRIEVANCE MODULE ----------------

def add_grievance():
    print("\nADD GRIEVANCE")

    gid = "G" + str(len(grievances) + 1)

    sid = input("Enter Student ID : ")
    category = input("Enter Category : ")
    desc = input("Enter Description : ")

    grievance = {
        "Grievance_ID": gid,
        "Student_ID": sid,
        "Category": category,
        "Description": desc,
        "Status": "Pending",
        "Date": datetime.now().strftime("%d-%m-%Y")
    }

    grievances.append(grievance)

    print("Grievance Submitted Successfully")
    print("Generated ID :", gid)


def view_grievances():
    print("\nALL GRIEVANCES")
    for g in grievances:
        print(g)


def update_status():
    gid = input("Enter Grievance ID : ")

    for g in grievances:
        if g["Grievance_ID"] == gid:
            status = input("Enter New Status : ")
            g["Status"] = status
            print("Status Updated")
            return

    print("Record Not Found")


# ---------------- REPORT MODULE ----------------

def pending_report():
    print("\nPENDING GRIEVANCES")

    for g in grievances:
        if g["Status"] == "Pending":
            print(g)


# ---------------- MAIN MENU ----------------

while True:
    print("\n====== SGRS MAIN MENU ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Grievance")
    print("4. View Grievances")
    print("5. Update Status")
    print("6. Pending Report")
    print("7. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        add_student()

    elif ch == "2":
        view_students()

    elif ch == "3":
        add_grievance()

    elif ch == "4":
        view_grievances()

    elif ch == "5":
        update_status()

    elif ch == "6":
        pending_report()

    elif ch == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
