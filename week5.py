students = {}
unique_ids = set()
logs = []

while True:
    print("\n1.Add Student")
    print("2.View")
    print("3.Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        sid = input("Enter ID : ")

        if sid not in unique_ids:
            name = input("Enter Name : ")
            dept = input("Enter Department : ")

            students[sid] = {
                "Name": name,
                "Department": dept
            }

            unique_ids.add(sid)
            logs.append(("Added", sid))

        else:
            print("ID Already Exists")

    elif ch == "2":
        print(students)
        print("Logs :", logs)

    elif ch == "3":
        break
