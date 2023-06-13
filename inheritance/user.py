#!/usr/bin/python3

class User: #parent class
    def __init__(self, name, email): # constructor method
        self.name = name
        self.email = email

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class Admin(User):
    def __init__(self, name, email, role):
        User.__init__(self, name, email)
        self.role = role

    def display(self):
        User.display(self)
        print(f"Role: {self.role}")

