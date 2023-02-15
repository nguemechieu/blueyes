
import datetime
import uuid as uuid


class Person(object):
    def __init__(self, name=None, age=None, email=None, password=None
                 , first_name=None, last_name=None, middle_name=None, phone=None, address=None):
        self.id = uuid.uuid1().hex
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.first_name = first_name
        self.las_name = last_name
        self.middle_name = middle_name
        self.phone = phone
        self.address = address
        self.dateCreated = datetime.datetime.fromtimestamp()





