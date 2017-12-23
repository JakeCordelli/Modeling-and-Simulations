import random

#The holding capacity of the party is 60 people
maxCapacity=60

#The longest the party is going to run for is 6 hours
maxDuration=6

#Maximum value of net change (at most, there will be a net change of 30)
maxGrowth=30
#Minimum value of net change (at the least, there will be a net change of -20)
minGrowth=-50

#A set turning point is defined that will determine when the flow of people out of the party becomes negative
#The turningPoint will occur somewhere between half past the max duration and the maxDuration
turningPoint=random.randrange(maxDuration/2, maxDuration)


                #All of the below arrays can be graphed to demonstrate the confined randomness as scatter plots
#Every iteration of the simulation, get the peak population, turning point,
#average size of party, overflow point, and party duration and add the elements
#to an their respected arrays
peakPopulations=[]          
turningPoints=[]                
averageSizeOfParties=[]     
overflowPoints=[]
partyDurations=[]

#Define how many times you want to run the simulation
global simRuns
simRuns=100


#Running sums of the averages in order to see graphs of convergence
runningAvgPeakPopulation=[]
runningAvgTurningPoint=[]
runningAvgAverageSizeOfParties=[]
runningAvgOverflowPoint=[]
runningAvgPartyDuration=[]


                                                #Functions needed

#In order to represent a positive change in population over time
def fillNetChanges(netChanges):
    #Fill the net changes array with positive values until the turing point
    for i in range(0, turningPoint):
        #Generate a positive integer between 1 and maxGrowth
        rPos = random.randrange(1, maxGrowth)
        netChanges.append(rPos)
    #When the turning point is reached, fill the rest of the array with negative values
    for i in range(turningPoint, maxDuration):
        #Generate a negative integer between minGrowth and 0
        rNeg = random.randrange(minGrowth, 0)  
        netChanges.append(rNeg)
    #print("Net Changes: ",  netChanges)



def fillPopLevels(popLevels, netChanges):
    #Calculate the running sum from netChanges and store the sum in popLevls
    for i in range(0,maxDuration):
        popLevels.append(sum(netChanges[0:i]))
        #If there is a number generated that exceeds the maxCapacity then convert it to maxCapacity
        if(popLevels[i]>=maxCapacity):
            popLevels[i]=maxCapacity
        if(popLevels[i]<=0):
            popLevels[i]=0
    #When the maximum duration is reached, everyone leaves the party 
    popLevels[maxDuration-1]=0
    
    #print ("Population Levels: ", popLevels)




def getPartyDuration(popLevels):
    #This temp array is used to hold the points of the popLevels array where the population is  0
    partyDurationTemp=[]
    for i in range(1, maxDuration-1): #New loop is defined to iterate past the first "0" in the list
        #If there is a negative value of population, change it to a zero
        if(popLevels[i]<=0):
            popLevels[i]=0
            partyDurationTemp.append(i)
            partyDuration=min(partyDurationTemp)
        else:
            partyDuration=maxDuration
    return(partyDuration)


def getOverflowPoint(popLevels, overflowPoint):
    #This temp array is used to hold the points of the popLevels array where the population = maxCapacity
    overflowTemp=[]
    for i in range(0, maxDuration):
        #Iterate the array to check to see if the value has reached maxCapacity
        if (popLevels[i]!=maxCapacity):
            overflowPoint=0
        else:
            overflowTemp.append(popLevels.index(60))

        #If the overflowTemp array is empty, return no overflow
        if (overflowTemp==[]):
            overflowPoint=0
        else:
            overflowPoint=min(overflowTemp)
    return(overflowPoint)


def printPartyInfo(peakPopLevels, turningPoint, averageLength, overflowPoint, partyDuration):
    print()
    print("Peak Population: ",peakPopLevels)
    print("Turning Point: ", turningPoint)
    print("Average size of party: ",averageLength)
    print("Overflow Point: ", overflowPoint)
    print("Party duration: ", partyDuration)        

#printPartyInfo()


def printAverages():

    #Take the averages of the array
    avgPeakPopulation=sum(peakPopulations)/simRuns
    avgTurningPoint=sum(turningPoints)/simRuns
    avgAverageSizeOfParties=sum(averageSizeOfParties)/simRuns
    avgOverflowPoint=sum(overflowPoints)/simRuns
    avgPartyDuration=sum(partyDurations)/simRuns


    
    print("Average Peak Population: ", avgPeakPopulation)
    print("Average Turning Point: ", avgTurningPoint)
    print("Average Utilization: {0:6.2f}".format(100*avgAverageSizeOfParties/maxCapacity), "%")
    print("Average Overflow Point: ", avgOverflowPoint)
    print("Average Party Duration: ", avgPartyDuration)


def main():
    count=0
    while(count<simRuns):
        count+=1
        #In order to ultimately calulate the averge time until overflow, we need to keep track of the overflow point
        #for each simulation of the party
        overflowPoint=0

        #The party does not always go until the end and will sometimes die down sooner
        #The partyDuration value will hold the length of time of the party
        partyDuration=0

        #Update Turning point
        turningPoint=random.randrange(maxDuration/2, maxDuration)

        #An array of size maxDuration that will hold the values of net change
        #These values are stored in an array for graphing purposes
        netChanges=[]       #Graph this

        #In order to keep track of the population, a running sum must be calculated from netChanges
        #The values of the running sum will be stored in the array popLevels
        popLevels=[]            #Graph this


        
        #Implement the fillNetChanges function to fill the netChanges array with the appropriate values
        fillNetChanges(netChanges)

        #Implement the fillPopLevels function to fill the popLevels array with the appropriate values
        fillPopLevels(popLevels, netChanges)

        

        #Get the average amount of people within the party at a given point in time
        averageLength=sum(popLevels)/(maxDuration-2)


        #Find the maximum amount of people in the party (peakPopLevels)
        peakPopLevels=max(popLevels)


        overflowPoint=getOverflowPoint(popLevels, overflowPoint)
        partyDuration=getPartyDuration(popLevels)


        
        #For each iteration of the simulation, store the values of interest into an array 
        peakPopulations.append(peakPopLevels)
        turningPoints.append(turningPoint)
        averageSizeOfParties.append(averageLength)
        overflowPoints.append(overflowPoint)
        partyDurations.append(partyDuration)

        #Add the values of interest to it's respective runningAverage array 
        runningAvgPeakPopulation.append(sum(peakPopulations)/len(peakPopulations))
        runningAvgTurningPoint.append(sum(turningPoints)/len(turningPoints))
        runningAvgAverageSizeOfParties.append(sum(averageSizeOfParties)/len(averageSizeOfParties))
        runningAvgOverflowPoint.append(sum(overflowPoints)/len(overflowPoints))
        runningAvgPartyDuration.append(sum(partyDurations)/len(partyDurations))



        #This will print the information for each instance of a party
        #print(popLevels)
        #print(netChanges)
        #printPartyInfo(peakPopLevels, turningPoint, averageLength, overflowPoint, partyDuration)
    
    print(simRuns, " Simulations")
    printAverages()

    #print(runningAvgOverflowPoint)



#Run the simulation 
main()
#print(runningAvgPeakPopulation)
#Conclusions:
#Average Peak Population:  54.17
#Average Turning Point:  4.17
#Average Utilization:  60.96 %
#Average Overflow Point:  2.54
#Average Party Duration:  6.0


#Notes:

#Something must be fixed because half the time, the average overflow point is a very low number when it
#should be roughly 2.5
