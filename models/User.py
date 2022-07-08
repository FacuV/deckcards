import logging

logging.basicConfig(filename='logs/user.log', level=logging.INFO)

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return "User: {} {} age: {}".format(self.first_name, self.last_name, self.age)
        