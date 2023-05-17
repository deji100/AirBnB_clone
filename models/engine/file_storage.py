#!/usr/bin/python3
"""Defines the FileStorage class model"""
import os
import json


class FileStorage:
    """A class for serializing or storing data and
    deserializing or retrieving data."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the all objs"""
        return self.__objects

    def new(self, obj):
        """
        Sets a new obj in __objects with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to a JSON file `file.json`"""
        with open(self.__file_path, mode="w") as f:
            storage = {}
            for k, v in self.__objects.items():
                storage[k] = v.to_dict()
            f.write(json.dumps(storage))

    def reload(self):
        """Deserializes a JSON file to __objects"""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(self.__file_path, encoding="utf-8") as f:
            storage = json.load(f)
            for obj in storage.values():
                self.new(eval(obj["__class__"])(**obj))
