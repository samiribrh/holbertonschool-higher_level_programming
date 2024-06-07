#!/usr/bin/python3
"""Module containing pickle module and CustomObject"""
import pickle


class CustomObject:
    """The CustomObject class"""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialization of instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Function to print attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Method to serialize the Object and write it to the file"""

        # None file case
        if not any(filename):
            return None

        # Serializing the data
        content = pickle.dumps(self)

        # Writing serialized data to the file
        with open(filename, 'wb') as file:
            file.write(content)

    @classmethod
    def deserialize(cls, filename):
        """Method to deserialize the Object from file"""

        # None file case
        if not any(filename):
            return None

        # Reading file content for deserialization
        with open(filename, 'rb') as file:
            content = file.read()

        # Returning deserialized data
        return pickle.loads(content)
