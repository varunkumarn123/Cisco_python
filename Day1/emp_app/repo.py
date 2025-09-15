employees = []  # [(id, name, age, salary, is_active)]


def create_employee(employee):
    global employees
    employees.append(employee)


def read_all_employee():
    return employees


def read_by_id(id):
    for employee in employees:
        if employee[0] == id:
            return employee
    return None


def update(id, new_employee):
    for i, employee in enumerate(employees):
        if employee[0] == id:
            employees[i] = new_employee
            break


def delete_employee(id):
    for i, employee in enumerate(employees):
        if employee[0] == id:
            employees.pop(i)
            break
