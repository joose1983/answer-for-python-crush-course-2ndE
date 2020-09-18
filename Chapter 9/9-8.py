class User:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"fist name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome! {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def display_login_attempts(self):
        print(f"user login attemtps are: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege=Privileges()
        
            

class Privileges:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
        
    def show_privileges(self):
        print(f"This user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        
user_admin=Admin('jackie','qin')
user_admin.privilege.show_privileges()


