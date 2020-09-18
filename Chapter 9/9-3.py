class User:

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print(f"fist name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome! {self.first_name} {self.last_name}")

user_jackie=User('jackie','qin')
user_tom=User('tom', 'nilson')

user_jackie.describe_user()
user_jackie.greet_user()

user_tom.describe_user()
user_tom.greet_user()
