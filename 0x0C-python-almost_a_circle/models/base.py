#!/usr/bin/python3
"""define my first class, the folder beocme a package"""
import json


class Base:
    """first class for a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define my initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string made out of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string representation"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            string = "[]"
        else:
            string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """return a list of the json string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n_rect = Rectangle(1, 1, 0, 0, 0)
            n_rect.update(**dictionary)
            return n_rect
        elif cls is Square:
            n_sqr = Square(1, 0, 0, 0)
            n_sqr.update(**dcitionary)
            return n_sqr

    def load_from_file(cls):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            with open("Rectangle.json", "r") as r:
                list_inst = Base.from_json_string(f.read())
            if list_inst == "":
                return []
            for index in range(len(list_instance)):
                list_inst[index] = Rectangle.create(**list_inst[index])

            return list_inst
        elif cls is Square:
            with open("Square.json", "r") as f:
                list_inst = Base.from_json_string(f.read())
            if list_inst == "":
                return []
            for index in range(len(list_inst)):
                list_inst[index] = Square.create(**list_insta[index])
            return list_insta
