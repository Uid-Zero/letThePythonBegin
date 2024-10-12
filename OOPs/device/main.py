from smartPhone import smartPhone
from laptop import laptop

def connectDevice(device):

    # Demonstrate device functionality. 
    print()
    print(device.deviceInfo())
    print(device.powerOn())
    print(device.checkBattery())
    print(device.connect())
    print()

# Demonstrating functionality
smartphoneInstance = smartPhone("Apple", "iPhone 15", "iOS 18", 20)
laptopInstance = laptop("Dell", "XPS 17", "Windows 12", True, 10)

# Polymorphism - both smartphone and laptop are instances of Device. 
connectDevice(smartphoneInstance)
connectDevice(laptopInstance)

# Additional methods showing unique behavior. 
print(smartphoneInstance.installApp("GitHub"))
print(laptopInstance.code("Python"))