def menu():
    print('1. Add employee')
    print('2. View employees')
    print('3. Search employee')
    print('4. Update employee')
    print('5. Delete employee')
    print('6. Exit')
    choice = input("Enter your choice (enter 'exit' to quit): ")
    if choice.lower() == 'exit':
        exit()
    return choice

def add_employees():
    with open('employees.txt', 'a') as file:
        employee_id = input('Enter employee id: ')
        employee_name = input('Enter employee name: ')
        employee_position = input('Enter employee position: ')
        employee_salary = input('Enter employee salary: ')
        file.write(f'Employee id: {employee_id}, Name: {employee_name}, Position: {employee_position}, Salary: {employee_salary}\n')
        print('Employee added successfully')

def view_employees():
    try:
        with open('employees.txt', 'r') as file:
            employees = file.readlines()
            if not employees:
                print('No employees found.')
            else:
                for employee in employees:
                    print(employee.strip())
    except FileNotFoundError:
        print('No employees found.')

def search_employee():
    employee_id = input('Search by employee id: ')
    found = False
    try:
        with open('employees.txt', 'r') as file:
            for line in file:
                if employee_id in line:
                    print(line.strip())
                    found = True
                    break
        if not found:
            print('Employee not found.')
    except FileNotFoundError:
        print('No employees found.')

def update_employee():
    employee_id = input('Update employee id: ')
    updated = False
    try:
        with open('employees.txt', 'r') as file:
            lines = file.readlines()
        with open('employees.txt', 'w') as file:
            for line in lines:
                if employee_id in line:
                    employee_name = input('Enter new employee name: ')
                    employee_position = input('Enter new employee position: ')
                    employee_salary = input('Enter new employee salary: ')
                    file.write(f'Employee id: {employee_id}, Name: {employee_name}, Position: {employee_position}, Salary: {employee_salary}\n')
                    updated = True
                else:
                    file.write(line)
        if updated:
            print('Employee updated successfully.')
        else:
            print('Employee not found.')
    except FileNotFoundError:
        print('No employees found.')

def delete_employee():
    employee_id = input('Delete employee id: ')
    deleted = False
    try:
        with open('employees.txt', 'r') as file:
            lines = file.readlines()
        with open('employees.txt', 'w') as file:
            for line in lines:
                if employee_id not in line:
                    file.write(line)
                else:
                    deleted = True
        if deleted:
            print('Employee deleted successfully.')
        else:
            print('Employee not found.')
    except FileNotFoundError:
        print('No employees found.')


# Main program loop
while True:
    menu_choice = menu()
    if menu_choice == '1':
        add_employees()
    elif menu_choice == '2':
        view_employees()
    elif menu_choice == '3':
        search_employee()
    elif menu_choice == '4':
        update_employee()
    elif menu_choice == '5':
        delete_employee()
    elif menu_choice == '6':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please try again.')