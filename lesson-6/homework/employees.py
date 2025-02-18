def employeeAdd():
    id = int(input("Enter Employee's ID: "))
    name = str(input("Employee's name: "))
    position = str(input("Employee's position: "))
    salary = int(input("Employee's salary: "))

    with open("employees.txt", "a") as employees:
        employees.write(f"{id}, {name}, {position}, {salary} \n")

    print("Employee added!")
    print("*" * 24)
#/////////////////

def viewEmployees():
    print("All Employees: ")
    employees = open("employees.txt", "r")
    print(employees.read())
    print("*" * 24)
#////////////////

def searchEmployees():
    search = int(input("Enter employee's ID: "))

    with open("employees.txt", "r") as employees:
        for x in employees:
            if x.startswith(str(search)):
                print("Employee's data: ")
                print(x)
                break
        else:
            print("The employee is not found")
    print("*" * 24)
#//////////////////

def updateEmployee():
    search = int(input("Enter employee's ID you want to update: "))

    with open("employees.txt", "r+") as employees:
        line = employees.readlines()
        for y, x in enumerate(line):
            if x.startswith(str(search)):
                updatedName = str(input("Enter new name: "))
                updatedPosition = str(input("Enter new position: "))
                updatedSalary = int(input("Enter new salary: "))

                line[y] = f"{search}, {updatedName}, {updatedPosition}, {updatedSalary} \n"
        employees.seek(0)
        employees.writelines(line)
    print("Employee updated")
    print("*" * 24)
#/////////////////////

def deleteEmployee():
    search = int(input("Enter employee's ID: "))

    with open("employees.txt", "r") as employees:
        line = employees.readlines()

    with open("employees.txt", "w") as employees:
        for x in line:
            if not x.startswith(str(search)):
                employees.writelines(x)
        print("Employee's data deleted!")
    print("*" * 24)
#////////////////////

def exit():
    employees =  open("employees.txt")
    employees.close()
    print("Exit!")
    print("*" * 24)
#//////////////////

while True:

    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    option = int(input("Choose one of the following options(1-6): "))

    if option == 1:
        employeeAdd()
    elif option == 2:
        viewEmployees()
    elif option == 3:
        searchEmployees()
    elif option == 4:
        updateEmployee()
    elif option == 5:
        deleteEmployee()
    elif option == 6:
        exit()
    else:
        print("Invalid option")