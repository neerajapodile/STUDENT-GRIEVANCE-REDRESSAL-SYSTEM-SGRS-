students = []

n = int(input("How many records to enter : "))

for i in range(n):
    print("\nEnter Student", i+1, "Details")

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

print("\nAll Records")
for s in students:
    print(s)

search_id = input("\nEnter Student ID to Search : ")

found = False

for s in students:
    if s["ID"] == search_id:
        print("\nRecord Found")
        print(s)
        found = True

if found == False:
    print("Record Not Found")
