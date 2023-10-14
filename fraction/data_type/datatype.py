
from abc import ABC, abstractclassmethod


class DataType(ABC):

    @abstractclassmethod
    def __init__(self):
        pass
    
    @abstractclassmethod
    def __add__(self):
        pass

    @abstractclassmethod
    def __sub__(self):
        pass

    @abstractclassmethod
    def __mult__(self):
        pass

    @abstractclassmethod
    def __truediv__(self):
        pass

    @abstractclassmethod
    def __eq__(self):
        pass

    @abstractclassmethod
    def __ne__(self):
        pass

    @abstractclassmethod
    def __lt__(self):
        pass

    @abstractclassmethod
    def __le__(self):
        pass

    @abstractclassmethod
    def __gt__(self):
        pass

    @abstractclassmethod
    def __ge__(self):
        pass

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass




