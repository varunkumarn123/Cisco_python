from db_setup import session, Employee
from log import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from exc import EmployeeNotFoundError, EmployeeAlreadyExistError, DatabaseError
#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App - Inmem array - dict element 
#employees = [] # [{'id':id,'name':name,'age':age,'salary':salary,'is_active':is_active}, ...]
def create_employee(employee):
    try: 
        employee_model = Employee(id = employee['id'],
                                    name = employee['name'],
                                    age = employee['age'],
                                    salary = employee['salary'],
                                    is_active = employee['is_active'])
        session.add(employee_model)#insert stmt db
        session.commit()
        logging.info("employee created")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate employee id:%s",ex)
        raise EmployeeAlreadyExistError(f'Employee id={employee['id']} exists already.')
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating employee:%s",ex)
        raise DatabaseError(f'Error in creating employee.')

def read_all_employee():
    employees = session.query(Employee).all()
    dict_employees = []
    for employee in employees:
        employee_dict = {'id':employee.id,'name':employee.name,
                         'age':employee.age, 'salary':employee.salary, 'is_active':employee.is_active}
        dict_employees.append(employee_dict)
    return dict_employees
    logging.info("read all employee")

def read_model_by_id(id):
    employee =session.query(Employee).filter_by(id = id).first()
    return employee 
    logging.info("read model by id")

def read_by_id(id):
    employee = read_model_by_id(id)
    if not employee:
        logging.info(f'Employee Not Found')
        return None
    employee_dict = {'id':employee.id,'name':employee.name,
                         'age':employee.age, 'salary':employee.salary, 'is_active':employee.is_active}
    return employee_dict
    logging.info('employee read by id')

def update(id, new_employee):#new_employee is update at id
    employee = read_model_by_id(id)
    if not employee:
        logging.info(f'Employee Not Found')
        return
    employee.salary =new_employee['salary']
    session.commit()
    logging.info("employee details updated")
    
def delete_employee(id):
    employee = read_model_by_id(id)
    if not employee:
        logging.info(f'Employee Not Found')
        return
    
    session.delete(employee)
    session.commit()
    logging.info('employee deleted')