#!/usr/bin/python3
"""Defines a BaseModel class inherited by other subclasses"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all subclasses to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Returns the string rep of an instance"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates self.updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""

        obj_dict = self.__dict__.copy()
        setattr(self, "__class__", type(self).__name__)
        setattr(self, obj_dict["created_at"],
                obj_dict["created_at"].isoformat())
        setattr(self, obj_dict["updated_at"],
                obj_dict["updated_at"].isoformat())

        return obj_dict
