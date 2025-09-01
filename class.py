class car:
    # Two underscore characters are required before and after 'init' to define the constructor
    # Self is the first parameter in the parameter list every method
    def __init__(self, n, e):   #constructor
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00 #Two underscore characters before an attribute name signify it  is private
    def SetPurchasePrice(self, p):
        self.__PurchasePrice = p
    def SetRegistration(self, r):
        self.__Registration = r
    def SetDateOfRegistration(self, d):
        self.__DateOfRegistration = d

    def GetVehicleID(self):
        return(self.__VehicleID)
    def GetRegistration(self):
        return(self.__Registration)
    def GetDateOfRegistration(self):
        return(self.__DateOfRegistration)
    def GetEngineSize(self):
        return(self.__EngineSize)
    def GetPurchasePrice(self):
        return(self.__PurchasePrice)

thiscar= car("ABC1234", 2500)
thiscar.SetPurchasePrice(12000)
thiscar.PurchasePrice = 12000
print(thiscar.GetVehicleID())
print(thiscar.PurchasePrice)

largesteng = 0
highestprice = 0
totalprice = 0
for i in range(5):
    caratt1= int(input("Enter VehicleID: "))
    caratt2= int(input("Enter the engine size: "))
    currentcar = car(caratt1, caratt2)
    currentcar.SetPurchasePrice(int(input("Set Purchase Price: ")))
    currentcar.SetRegistration(int(input("Set Registration Number: ")))
    currentcar.SetDateOfRegistration(input("Set the Date of Registration: "))

    if highestprice < currentcar.GetPurchasePrice():
        highestprice = currentcar.GetPurchasePrice()
    if largesteng < currentcar.GetEngineSize():
        largesteng = currentcar.GetEngineSize()
    
    totalprice = totalprice + currentcar.GetEngineSize()
    print("Toyota: ", currentcar.GetVehicleID())
    print("Registration Number: ", currentcar.GetRegistration())
    print("Date of Registration: ", currentcar.GetDateOfRegistration())
    print("Engine Size: ", currentcar.GetEngineSize())
    print("Purchase Price: ", currentcar.GetPurchasePrice())

avgprice = totalprice / 5
print(highestprice)
print(avgprice)
print(largesteng)

carjobs1 = [Car("",0) for i in range (5)]
carobjs2= []
car1= Car("Abcd",3455)
for i in range (2):
    caratt1= int(input("Enter VehicleID: "))
    caratt2= int(input("Enter the engine size: "))
    carobjs2.append(Car(caratt1,caratt2))
for i in range (len(carobjs2)):
    print("\nPlease enter the Purchase price for", carobjs1[i].GetVehicleID())
    pprice = input()
    carobjs1[i].SetPurchasePrice(pprice)

    print("Please enter the Registration No for", carobjs1[i].GetVehicleID())
    regno = input()
    carobjs1[i].SetRegistration(regno)

    print("Please enter the Date of Registration for", carobjs1[i].GetVehicleID())
    date = input()
    carobjs1[i].SetDateofRegistration(date)

# display carobjs1 details
print("\n--- Carobjs1 Details ---")
for i in range(len(carobjs1)):
    print("Vehicle ID:", carobjs1[i].GetVehicleID())
    print("Registration No:", carobjs1[i].GetRegistration())
    print("Date of Registration:", carobjs1[i].GetDateofRegistration())
    print("Engine Size:", carobjs1[i].GetEngineSize())
    print("Purchase Price:", carobjs1[i].GetPurchasePrice())
    print()

# allow user to search in carobjs2
carToDisplay = input("Please enter Vehicle ID of car to view the details: ")

for i in range(len(carobjs2)):
    if carToDisplay == carobjs2[i].GetVehicleID():
        print("\n--- Car Found ---")
        print("Vehicle ID:", carobjs2[i].GetVehicleID())
        print("Registration:", carobjs2[i].GetRegistration())
        print("Date of Registration:", carobjs2[i].GetDateofRegistration())
        print("Engine Size:", carobjs2[i].GetEngineSize())
        print("Purchase Price:", carobjs2[i].GetPurchasePrice())
