
class car:
    def __init__(self, arrivalTime, departureTime):
        self.arrivalTime=arrivalTime
        self.departureTime=departureTime
        self.lotSize=30
        self.parkingLot=[]
        self.carCount=0
    
    def parkCar(self,):
        self.parkingLot.append(1)

    def carLeaves(self):
        return self.parkingLot.pop()

    def fillLot(self):
       for i in range (self.lotSize):
           self.parkingLot.append(1)

    def emptyLot(self):
        for i in range (self.lotSize):
            return self.parkingLot==[]

    def carsInLot(self):
        for i in range(self.lotSize):
            if (self.parkingLot[i]==1):
                self.carCount=self.carCount+1
        print(self.carCount)
        return (self.carCount)

    def showLot(self):
        print(self.parkingLot)
        return (self.parkingLot)

    def fullInfo(self):
        print("Parking Lot: ")
        self.showLot()
        print()
        print("Cars in Lot: ",)
        self.carsInLot()

"""Arrival/Departure times are randomly generated"""
c=car(2, 5)
c.fillLot()
c.parkCar()
c.fullInfo()

"""Add in parameters that will not allow the parking lot to be added to if it is at capacity"""
"""Create an overfill counter and add to it when a car attempts to enter at capacity"""
"""Create a lostCustomer counter (.5 of the people who come when the lot is full leave)"""
