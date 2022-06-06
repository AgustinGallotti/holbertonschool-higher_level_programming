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
        """funciton explained"""
        """---from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            n_rect = Rectangle(1, 1, 0, 0, 0)
            n_rect.update(**dictionary)
            return n_rect
        elif cls is Square:
            n_sqr = Square(1, 0, 0, 0)
            n_sqr.update(**dcitionary)
            return n_sqr---"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        try:    
            with open(filename, "r") as f:
                return [cls.create(**obj) for obj
                        in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
