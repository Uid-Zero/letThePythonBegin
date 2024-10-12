from device import device

class laptop(device):
    def __init__(self, brand, model, os, isTouchscreen, batteryLife):
        super().__init__(brand, model)
        self.__os = os
        self.__isTouchscreen = isTouchscreen
        self.__batteryLife = batteryLife

    def deviceInfo(self):
        touchscreenStatus = "Touchscreen" if self.__isTouchscreen else "Non-Touchscreen"
        return f"Laptop: {self.getBrand()} {self.getModel()} ({touchscreenStatus}) running {self.__os}, Battery life: {self.__batteryLife} hours"

    def connect(self):
        return "Connecting to Wi-Fi network..."

    def powerOn(self):
        return f"Powering on {self.getBrand()} {self.getModel()}"

    def code(self, language):
        return f"Writing {language} code on {self.getBrand()} {self.getModel()}"

    def checkBattery(self):
        return f"Battery life remaining: {self.__batteryLife} hours"