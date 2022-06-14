#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Base class  """
import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of
        list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        to_write = []
        if list_objs is not None:
            for objs in list_objs:
                to_write.append(cls.to_dictionary(objs))
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
