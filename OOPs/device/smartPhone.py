from device import device

class smartPhone(device):
    def __init__(self, brand, model, os, batteryLife):
        super().__init__(brand, model)
        self.__os = os
        self.__batteryLife = batteryLife

    def deviceInfo(self):
        return f"Smartphone: {self.getBrand()} {self.getModel()} running {self.__os}, Battery life: {self.__batteryLife} hours"

    def connect(self):
        return "Connecting to cellular network..."

    def powerOn(self):
        return f"Powering on {self.getBrand()} {self.getModel()}"

    def installApp(self, appName):
        return f"Installing {appName} on {self.getBrand()} {self.getModel()}"

    def checkBattery(self):
        return f"Battery life remaining: {self.__batteryLife} hours"