students = []

def add_student():
    name = input("Enter Name : ")
    sid = input("Enter ID : ")
    dept = input("Enter Department : ")
    issue = input("Enter Issue : ")

    students.append({
        "Name": name,
        "ID": sid,
        "Department": dept,
        "Issue": issue
    })

    print("Student Added")

def view_students():
    for s in students:
        print(s)

def search_student():
    sid = input("Enter ID to Search : ")

    for s in students:
        if s["ID"] == sid:
            print(s)

def delete_student():
    sid = input("Enter ID to Delete : ")

    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("Deleted")

while True:
    print("\n1.Add")
    print("2.View")
    print("3.Search")
    print("4.Delete")
    print("5.Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        delete_student()
    elif ch == "5":
        break
