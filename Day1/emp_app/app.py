#1. testing the repo.py
import repo
employee = (101,'Banu',22,5000,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('After add:', repo.read_all_employee())


employee = (102,'mahesh', 45,4000,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('After add:', repo.read_all_employee())

employee = (103,'Vaishnavi',21,5000,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('After add:', repo.read_all_employee())

#test read by id

employee = repo.read_by_id(103)
if employee == None:
    print("Employee not found")
else:
    id, name, age, salary, is_active = employee
    salary += 2000
    new_employee = (id, name, age, salary, is_active)
    repo.update(103,new_employee)
    print('After update', repo.read_all_employee())

# test delete
repo.delete_employee(102)
print("After delete:", repo.read_all_employee())