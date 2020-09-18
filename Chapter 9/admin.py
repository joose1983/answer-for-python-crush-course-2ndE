from user import User
from priviledges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviledge=Privileges()
