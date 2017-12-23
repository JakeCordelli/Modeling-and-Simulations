import random
from math import log


def putSeed():
    random.seed(123456789)

def newRandom():
    x = random.random()
    return x

def Exponential(m):
    return (-m * log(1.0 - newRandom()))


def listOf1000():
    #array that holds 1000 randomly generated values
    x = []

    m=0

    #Running total of the average at each location of the list
    avg=[]

    #array that holds all of the converging values
    converge = []

    #array that holds the smallest value from each array
    smalls = []

    #create a garbage array
    garbage=[]


    for i in range(0, 1000):
        j = Exponential(9)
        x.append(j)

        #keep track of the current average with each iteration
        avg.append(sum(x) / len(x))

        # If the average falls within 1% of the known convergence
        if (8.999 < avg[i] < 9.001):

            # Add the location of that value to the convergence array
            converge.append(i)

        else:
            pass
        #print(avg[i])
    #Find the smallest value of convergence
    #If the convergence array is empty, pass. Else, find the min(convergence)
    if (converge==[]):
        pass
    else:
        m=min(converge)
    #print(m)


    #Return the smallest value of a randomly generated array
    return (m)
    # Conclusion: The function converges to 9


#Takes in the output of listOf1000() and will return a new list of the smallest convergence values
def listOfSmallest():
    list=[]

    #Generate a list of size n (in this case 100)
    for i in range (100):
        x=listOf1000()
        list.append(x)

    #Return the list of the smallest values captured from 100 simulations of listOf1000()
    l=min(list)
    h=max(list)
    return (l, h)

"""
def genAvgSmalls():
    # finalSmalls holds the array of smallest convergence values
    finalSmalls = []

    # Looks at the averages of the smallest value in 100 lists
    for i in range(1, 100):
        finalSmalls.append(listOf1000())
    # print(finalSmalls)

    # flatten the generated list of lists
    fSmalls = [item for sublist in finalSmalls for item in sublist]
    avgSmallestConvergence = sum(fSmalls) / len(fSmalls)

    # print(avgSmallestConvergence)
    return (avgSmallestConvergence)

def rangeOfConvergence():
    x = []
    # collect 10 instances of the smallest convergence value and store in x
    for i in range(100):
        x.append(genAvgSmalls())
    # With min and max, the range of convergence is found
    print("The range of convergence is: ", min(x), "-", max(x))
    print("\n")
"""


def main():
    listOf1000()
    print(listOfSmallest())


main()
