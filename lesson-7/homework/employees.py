import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        print("Employee Records:")
        for record in records:
            print(record.strip())

    @staticmethod
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated = False
        records = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts[0] == str(employee_id):
                    if name:
                        parts[1] = name
                    if position:
                        parts[2] = position
                    if salary:
                        parts[3] = str(salary)
                    updated = True
                records.append(", ".join(parts))
        if updated:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.write("\n".join(records) + "\n")
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        records = []
        deleted = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id) + ","):
                    records.append(line.strip())
                else:
                    deleted = True
        if deleted:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.write("\n".join(records) + "\n")
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def menu():
        while True:
            print("\nEmployee Records Manager")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                EmployeeManager.add_employee(Employee(emp_id, name, position, salary))
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(emp_id)
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new name (press Enter to keep current): ") or None
                position = input("Enter new position (press Enter to keep current): ") or None
                salary = input("Enter new salary (press Enter to keep current): ") or None
                EmployeeManager.update_employee(emp_id, name, position, salary)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(emp_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the menu
if __name__ == "__main__":
    EmployeeManager.menu()
