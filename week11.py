# WEEK 11

def validate_id():
    sid = input("Enter Student ID : ")

    if sid == "":
        raise ValueError("ID Cannot Be Empty")

    return sid


def validate_name():
    name = input("Enter Name : ")

    if name.isalpha() == False:
        raise ValueError("Only Letters Allowed")

    return name


def validate_age():
    age = int(input("Enter Age : "))

    if age <= 0 or age > 100:
        raise ValueError("Invalid Age")

    return age


while True:
    try:
        sid = validate_id()
        name = validate_name()
        age = validate_age()

        print("\nValidated Data")
        print("ID :", sid)
        print("Name :", name)
        print("Age :", age)
        break

    except ValueError as e:
        print("Error :", e)

    except Exception:
        print("Unexpected Error")


# File Handling Exception

try:
    file = open("grievances.csv", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("CSV File Not Found")
