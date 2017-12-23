from fractions import gcd
"""Enter a prime number value for m"""
m=127

"""(2.2.1)Determine if something is full period multiplier (a)"""
"""Generate a list of numbers to test"""
n=100
z=list(range(1, n))

"""initialize new array to store full period multiplier"""
r=[]
"""(j) is a value in the testing list"""
def FPM(j):
    p=1
    a=j
    x=a
    while(x!=1):
        p=p+1
        x =(a*x)%m
    if (p==m-1):
        r.append(a)

"""increments through the list to see if anything is a full period multiplier"""
for i in range (0, len(z)):
    FPM(z[i])

"""Prints the list of FPMs"""
print("FPMs from 1 to ", n) 
print(r)

"""Returns the values 3, 6, and 7"""
"""Once the FPMs are received, they can be fed into the next algorithm"""

"""(2.1.2)Given a prime number (m) and any full period multiplier (a), this generates all FPMs relative to (m)"""
o=[]
for k in range(0, len(r)):
    i=1
    x=r[k]
    while (x!=1):
        if (gcd(i, m-1)==1):
            print (x, " is a full period multiplier equal to ", r[k],"^",i, "%",m)
            o.append(x)
        i=i+1
        x=(r[k]*x)%m

"""Prints the amount of instances of a FPM"""
print("\nFound ", len(o), " FPMs")

"""Prints the list of FPMs with respect to m"""
print("List of FPMs with respect to m: \n", o)
