from .db_setup import session, Flight
from .log import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exc import FlightNotFoundError, FlightAlreadyExistError, DatabaseError
#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App - Inmem array - dict element 
#employees = [] # [{'id':id,'name':name,'age':age,'salary':salary,'is_active':is_active}, ...]
def create_flight(flight):
    try: 
        flight_model = Flight(id = flight['id'],
                                    name = flight['name'],
                                    age = flight['age'],
                                    salary = flight['salary'],
                                    is_active = flight['is_active'])
        session.add(flight_model)#insert stmt db
        session.commit()
        logging.info("flight created")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate flight id:%s",ex)
        raise FlightAlreadyExistError(f'Flight id={flight['id']} exists already.')
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating flight:%s",ex)
        raise DatabaseError(f'Error in creating flight.')

def read_all_flight():
    flights = session.query(Flight).all()
    dict_flights = []
    for flight in flights:
        flight_dict = {'id':flight.id,'name':flight.name,
                         'age':flight.age, 'salary':flight.salary, 'is_active':flight.is_active}
        dict_flights.append(flight_dict)
    return dict_flight
    logging.info("read all flight")

def read_model_by_id(id):
    flight =session.query(Flight).filter_by(id = id).first()
    return flight 
    logging.info("read model by id")

def read_by_id(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f'flight Not Found')
        return None
    flight_dict = {'id':flight.id,'name':flight.name,
                         'age':flight.age, 'salary':flight.salary, 'is_active':flight.is_active}
    return flight_dict
    logging.info('flight read by id')

def update(id, new_flight):#new_employee is update at id
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f'flight Not Found')
        return
    flight.salary =new_flight['salary']
    session.commit()
    logging.info("flight details updated")
    
def delete_flight(id):
    flight = read_model_by_id(id)
    if not flight:
        logging.info(f'flight Not Found')
        return
    
    session.delete(flight)
    session.commit()
    logging.info('flight deleted')