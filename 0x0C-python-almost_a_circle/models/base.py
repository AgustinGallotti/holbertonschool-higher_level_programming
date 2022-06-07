#!/usr/bin/python3
"""define my first class, the folder beocme a package"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function ot save file"""
        if list_objs:
            filename = cls.__name__ + ".csv"
            with open(filename, "w") as f:
                if "Rectangle" in filename:
                    fields = ["id", "width", "height", "x", "y"]
                elif "Square" in filename:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """define load"""
        filename = cls.__name__ + ".csv"
        if (filename):
            if "Rectangle" in filename:
                fields = ["id", "width", "height", "x", "y"]
            elif "Square" in filename:
                fields = ["id", "size", "x", "y"]
            list_objs = []
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if len(fields) == 4:
                        n_inst = cls(1)
                    elif len(fields) == 5:
                        n_inst = cls(1, 1)
                    for a, field in enumerate(row):
                        setattr(n_inst, fields[a], int(row[field]))
                    list_objs.append(n_inst)
            return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """drawings"""
        from turtle import Turtle, Screen
        from time import sleep

        screen = Screen()
        tor.fillcolor("white")
        tor.begin_fill()
        for side in range(4):
            tor.forward(100)
            tor.left(90)
        tor.end_fill()
    tor.penup()
    tor.goto(-350, 0)
    tor.pendown()

    while True :
        tor.clear()
        draw()

        screen.update()
        tor.forward(0.2)
