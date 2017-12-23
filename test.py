
#import the random libraries for random number generation (uniform)
import random

#import the matplotlib libraries for graphing of the data 
"""import matplotlib.pyplot as plt"""

#The values for this simulation come from logical observations of house parties.

#The holding capacity of the party is 60 people
maxVal = 60  # 

#The longest the party is going to run for is 6 hours
maxDuration = 6

#An array of size maxDuration that will hold the values of net change
#These values are stored in an array for graphing purposes
netChanges = [] * maxDuration

#Maximum value of net change (at most, there will be a net change of 30)
maxGrowth=30

#Minimum value of net change (at the least, there will be a net change of -20)
minGrowth=-20

saturationPoints=[]

turningPoint=0


#Arrays to hold the averages of the data we are interested in
#In particular, we want to know the average turning point of the party, the average highest population point,
#the average duration of a party, the average population of a party at a point in time, and the times at which
#a saturation point has been reached
avgTurningPoints = []
averageMaxPopulations = []
averagePartyLengths = []
averageSizeOfParties = []
averageSaturationPoints = []


#method that adds a value to the netChange array 
def add_to_array(x):
    netChanges.append(x)

#In order to represent a positive change in population over time
#Generate a positive integer between 1 and maxDuration
def RNGpos():
    rPos = random.randrange(0, maxGrowth)  
    return (rPos)  

#In order to represent a negative change in population over time
#Generate a positive integer between 1 and maxDuration
def RNGneg():
    rNeg = random.randrange(minGrowth, 0)  # returns a negative rate
    return (rNeg)

#Get the current population of the party over time
def getCurrentPop():
    runningSum=[]*maxDuration
    for i in range(1, len(netChanges)):
        runningSum.append(sum(netChanges[:i]))

    #Turn any negative values into zeros
    for i in range(1, maxDuration):
        if (runningSum[i]<=0):
            runningSum[i]=0
            runningSum.remove(0)


    #In order to prevent the party size from exeding maxVal
    #Turn any values greater than maxVal into maxVal
    #This creates a pleateu effect on the graph
    for i in range(0, len(runningSum)):
        if (runningSum[i]>=maxVal):
            runningSum[i]=maxVal


        #If there are still people at the party, kick them all out
        if (runningSum[len(runningSum)-1]!=0):
            runningSum[len(runningSum)-1]=0

    return (runningSum)


def getSaturationPoint():
    j=getCurrentPop()
    for i in range(1, getTimePartyOver()):
        if (j[i]>=maxVal):
            #Saturation point occurs when current populaiton reaches maxVal
            saturationPoints.append(i)
        else:
            saturationPoints.append(1)
    return (min(saturationPoints))


#Returns the time at which the population returns to 0
def getTimePartyOver():
    x=[]
    #Get the point in time where there are 0 or fewer people at the party
    for i in range(0, len(getCurrentPop())):
        if (getCurrentPop()[i]<=0):
            x.append(i)
    if (sum(x)==0):
        return (1)
    else:
        if (x==[]):
            return (1)
        else:
            return (min(x))

def main():
    #In order to decide upon a point at which the rate transfers from positive to negative
    #Generate an integer between 1 hour and half the maxDuration 
    turningPoint = random.randrange(1, maxDuration)

    count=0
    while(count<1):
        count=count+1

        #while the time is less than the turning point, add positive values
        for i in range(0, turningPoint):
            add_to_array(RNGpos())

        #while the time is greater than the turning point, add negative values
        for i in range(turningPoint, maxDuration):
            add_to_array(RNGneg())

        maxPopulation = max(getCurrentPop())
        partyDuration = getTimePartyOver()
        partySize = sum(getCurrentPop()[0:5])/getTimePartyOver()
        timeToSaturation = getSaturationPoint()

        avgTurningPoints.append(turningPoint)
        averageMaxPopulations.append(maxPopulation)
        averagePartyLengths.append(partyDuration)
        averageSizeOfParties.append(partySize)
        averageSaturationPoints.append(timeToSaturation)

        printInfo()

#Print all of the information about the system to the console
def printInfo():
    print("Current Pop over time: ", getCurrentPop())
    print("Turning Point: ", turningPoint, "hours")
    print("Net rate over time: ", netChanges)
    print("Maximum population acheived: ", max(getCurrentPop()), " people")
    print("Maximum rate acheived: ", max(netChanges), " people per hour")
    print("Party length: ", getTimePartyOver(), " hours")        
    print("Average size of party: ", sum(getCurrentPop()/getTimePartyOver()))
    print("Time to Saturation: ", getSaturationPoint() ," hours")


    #Using matplotlib, plot the appropriate graphs
    """
    #Plotting for the growth over time
        plt.plot(netChanges)
        plt.ylabel('rates over time')
        plt.show()

    #Plotting for the population over time
        plt.plot(getCurrentPop())
        plt.ylabel('Population over time')
        plt.show()
    """

main()



"""Working on constructing averages"""
def printAverages():
    #Print Averages
    print()
    print("avgTurningPoint: ", sum(avgTurningPoints)/len(avgTurningPoints))
    print("averageMaxPopulation: ", sum(averageMaxPopulations)/len(averageMaxPopulations))
    print("averagePartyDuration: ", sum(averagePartyLengths)/len(averagePartyLengths))
    print("averagePopulationInParty: ", sum(averageSizeOfParties)/len(averageSizeOfParties))
    print("averageSaturationPoint: ", sum(averageSaturationPoints)/len(averageSaturationPoints))


printAverages()
print(getCurrentPop())
#Notes
#There is currently a coding issue with the average saturation point calculation (does not return correctly)


