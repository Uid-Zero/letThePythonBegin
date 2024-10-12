from abc import ABC, abstractmethod

class device(ABC):
    def __init__(self, brand, model):
        # Initialize brand and model attributes
        self.__brand = brand
        self.__model = model
    
    def getBrand(self):
        # Getter method for brand
        return self.__brand

    def getModel(self):
        # Getter method for model
        return self.__model

# Abstract method to be implemented by subclasses:

    @abstractmethod
    def deviceInfo(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def powerOn(self):
        pass