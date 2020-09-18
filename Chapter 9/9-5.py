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

        
user_jackie=User('jackie','qin')
user_jackie.increment_login_attempts()
user_jackie.display_login_attempts()
user_jackie.increment_login_attempts()
user_jackie.display_login_attempts()
user_jackie.increment_login_attempts()
user_jackie.display_login_attempts()
user_jackie.reset_login_attempts()
user_jackie.display_login_attempts()


