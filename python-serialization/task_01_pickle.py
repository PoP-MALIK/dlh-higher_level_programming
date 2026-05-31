#!/usr/bin/python3
"""Module that defines a CustomObject class with pickle serialization."""
import pickle


class CustomObject:
    """A custom class with pickle serialization and deserialization."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a pickle file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The deserialized object, or None if error.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
