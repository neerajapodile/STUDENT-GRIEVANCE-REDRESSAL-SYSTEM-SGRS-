students = []

while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Student Grievance")
    print("2. View All Grievances")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        name = input("Enter Name : ")
        sid = input("Enter ID : ")
        dept = input("Enter Department : ")
        issue = input("Enter Issue : ")

        record = {
            "Name": name,
            "ID": sid,
            "Department": dept,
            "Issue": issue
        }

        students.append(record)
        print("Grievance Added Successfully")

    elif choice == "2":
        print("\n--- All Grievances ---")
        for s in students:
            print(s)

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
