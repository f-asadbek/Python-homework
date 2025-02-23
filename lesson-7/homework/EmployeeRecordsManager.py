import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        self.employees = []
        self.load_employees()

    def load_employees(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(", ")
                    if len(data) == 4:
                        self.employees.append(Employee(data[0], data[1], data[2], float(data[3])))

    def save_employees(self):
        with open(self.FILE_NAME, "w") as file:
            for employee in self.employees:
                file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")

    def add_employee(self):
        while True:
            employee_id = input("Enter Employee ID: ")
            if any(emp.employee_id == employee_id for emp in self.employees):
                print("Error: Employee ID already exists! Try again.")
            else:
                break

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))

        new_employee = Employee(employee_id, name, position, salary)
        self.employees.append(new_employee)
        self.save_employees()
        print("Employee added successfully!")

    def view_all_employees(self):
        if not self.employees:
            print("No employee records found.")

        print("Sort by:")
        print("1. Name")
        print("2. Salary")
        sort_choice = input("Choose an option (1 or 2): ")

        if sort_choice == "1":
            sorted_employees = sorted(self.employees, key=lambda emp: emp.name)
        elif sort_choice == "2":
            sorted_employees = sorted(self.employees, key=lambda emp: emp.salary, reverse=True)
        else:
            print("Invalid choice, displaying unsorted records.")
            sorted_employees = self.employees

        print("\nEmployee Records:")
        for employee in sorted_employees:
            print(employee)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("Employee Found:", employee)
        print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        for employee in self.employees:
            if employee.employee_id == employee_id:
                new_name = input("Enter new Name: ")
                new_position = input("Enter new Position: ")
                new_salary = input("Enter new Salary: ")

                employee.salary = float(new_salary)
                employee.name = new_name if new_name else employee.name
                employee.position = new_position if new_position else employee.position

                self.save_employees()
                print("Employee updated successfully!")
        print("Error: Employee not found!")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        if any(emp.employee_id == employee_id for emp in self.employees):
            self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
            self.save_employees()
            print("Employee deleted successfully!")
        else:
            print("Error: Employee not found!")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
