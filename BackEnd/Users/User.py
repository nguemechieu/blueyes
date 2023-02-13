import  logging
import datetime
import uuid as uuid
class User(object):
    def __init__(self):
        self.email = "noel@live.com"
        self.username = "n"
        self.password = "password"
        self.phone = "234-34-2390"
        self.first_name = "xno"
        self.last_name = "ma"
        self.middle_name = "mas"
        self.birthday = date.today()
        self.id =  uuid.uuid4().hex();
        self.created_at = datetime.datetime.fromtimestamp
        self.updated_at = datetime.datetime.fromtimestamp



