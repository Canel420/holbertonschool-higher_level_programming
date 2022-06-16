#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Base class  """
from ctypes import py_object
import json
import csv


class Base:
    """
    This base class of all
    other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts to JSON string """
        if list_dictionaries is None or not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_args):
        """
        writes the JSON string representation of
        list_args to a file.
        """
        filename = cls.__name__ + ".json"
        to_write = []
        if list_args is not None:
            for args in list_args:
                to_write.append(cls.to_dictionary(args))
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(to_write))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string representation """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, 'r', encoding='utf-8')as file:
                instance_list = cls.from_json_string(file.read())
            for key, val in enumerate(instance_list):
                instance_list[key] = cls.create(**instance_list[key])
        except FileNotFoundError:
            pass
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_args):
        """ Python object to csv object. """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if cls.__name__ == 'Rectangle':
                for args in list_args:
                    writer.writerow([args.id, args.width,
                                     args.height, args.x, args.y])
            elif cls.__name__ == 'Square':
                for args in list_args:
                    writer.writerow([args.id, args.size, args.x, args.y])

    @classmethod
    def load_from_file_csv(cls):
        """ csv object to python object. """
        filename = cls.__name__ + ".csv"
        objects = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for args in reader:
                    if cls.__name__ == 'Rectangle':
                        py_object = {
                            'id': int(args[0]),
                            'width': int(args[1]),
                            'height': int(args[2]),
                            'x': int(args[3]),
                            'y': int(args[4])}
                    elif cls.__name__ == 'Square':
                        py_object = {
                            'id': int(args[0]),
                            'size': int(args[1]),
                            'x': int(args[2]),
                            'y': int(args[3])}
                    objs = cls.create(**py_object)
                    objects.append(objs)
        except FileNotFoundError:
            pass
        return objects
