import random
import matplotlib.pyplot as plt

maxVal = 60 #holding capacity
maxDuration=10
myArray=[]*maxDuration


def getSizeofArray():
    return(len(myArray))

def add_to_array(x):
    myArray.append(x)

def RNGpos():
    rPos=random.randrange(1, 10) #random net change
    return (rPos) #random net change
    
def RNGneg():
    rNeg = random.randrange(-10, 0) #returns a negative rate
    return (rNeg)
    
def getAverageDuration():
    return 'median'
    
def sumMyArray():
    print (sum(myArray))
    
def getTurningPoint():
    turningPoint=random.randrange(1, maxDuration/2)
    return (turningPoint)


if __name__ == '__main__':
    turningPoint=getTurningPoint()
    for i in range(0, turningPoint):
   	 add_to_array(RNGpos())
   	 
    for i in range(turningPoint, maxDuration):
   	 add_to_array(RNGneg())
"""
    for i in range(len(myArray)):
   	 runningSum=0
   	 runningSum = sum(myArray[i])
   	 runningAverage = runningSum/i
   	
   	 #if (runningSum>=maxVal):
   		 #full=true
"""
print("Turning Point: ", turningPoint)
print(myArray)
#Plotting
plt.plot(myArray)
plt.ylabel('rates over time')
plt.show()
   	 
#
#    if (sumMyArray >= maxVal):
#   	 then full = true
#
