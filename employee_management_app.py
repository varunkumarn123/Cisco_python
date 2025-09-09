employees = [] #list()
employee = ('Banu',22,5000,True)
employees.append(employee)
employee = ('mahesh', 45,4000,True)
employees.append(employee)
employee = ('Vaishnavi',21,5000,True)
employees.append(employee)


i=0
search = 'Vaishnavi'
index = -1
for emp in employees:
    if emp[0] == search:
        index = i
        break
    i +=1

if index == -1
    print("Employee Not Found")
else:
    search_employee = employees[index]
    print(search_employee)
    salary = float(input("Salary"))
    employee = (search_employee[0],search_employee[1],search_employee[2])
    employees[index] = employee
print('after search and update:', employees)


employee = ('Dravid', 50, 200.75, True)
employees.append(employee)
print('after add Dravid:', employees)
employees.pop() #delete the last emplo
print('after delete Dravid:', employee) #[Banu..Mahesh..,Vaishnavi]

#delete employee Mahesh by position

position = 1
employees.pop(position) #delete the last employee
print('after delete Mahesh:', employees) #[Banu..,Vaishnavi..]
