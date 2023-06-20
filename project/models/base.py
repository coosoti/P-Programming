#!/usr/bin/python3

import json

class Base:
    # private class attribute __count is initialized to 0 
    # and it track of the number of Base objects that have been created
    # without an explicit id value
    __nb_objects = 0

    def __init__(self, id=None):
        """this constructor method creates a instance of Base class object
        Args:
            id (int): Optional id of the instant to be created.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries if list_dictionaries is not None else [])

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        list_objects = [cls.to_dictionary(obj) for obj in list_objs] if list_objs else []
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_objects))










