import requests
import json
from flask_sqlalchemy import SQLAlchemy

NR_OF_PERSON_TO_SEED = 500
SEED = 'abc'

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    age = db.Column(db.String(30))
    street_name = db.Column(db.String(100))
    street_number = db.Column(db.String(20))
    postcode = db.Column(db.String(30))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(30))
    pictures = db.relationship('EmployeePicture', back_populates='employee', lazy=True)

class EmployeePicture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture_size = db.Column(db.String(100))
    picture = db.Column(db.String(100))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employee = db.relationship('Employee', back_populates='pictures', lazy=True)


def seed_data(db):


    if not Employee.query.count():
        r = requests.get(f'https://randomuser.me/api/?results={NR_OF_PERSON_TO_SEED}&seed={SEED}')
        if not r.status_code == 200:
            raise ValueError('Unable to fetch data! Status code not 200!')
        
        data = json.loads(r.text)
        list_of_persons = data['results']

        for person in list_of_persons:
            new_employee = Employee(
                            name = person['name']['first'] + ' ' + person['name']['last'],
                            email = person['email'],
                            phone = person['phone'],
                            age = person['dob']['age'],
                            street_name = person['location']['street']['name'],
                            street_number = person['location']['street']['number'],
                            postcode = person['location']['postcode'],
                            city = person['location']['city'],
                            state = person['location']['state'],
                            country = person['location']['country']
            )
            db.session.add(new_employee)
            db.session.commit()
            for key,val in person['picture'].items():
                p = EmployeePicture(
                        picture_size = key,
                        picture = val,
                        employee_id = new_employee.id
                )                
                db.session.add(p)
            db.session.commit()


