from abc import ABC, abstractmethod

class Load(ABC):

    def __init__(self, magnitude, start_location, end_location):
        self.magnitude = magnitude
        self.start_location = start_location
        self.end_location = end_location
