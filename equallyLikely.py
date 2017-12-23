import random

'''Used to simulate the rolling of one die'''
def equallyLikely(x, y):
    j=random.randrange(x, y+1)
    return(j)


'''Iterate rolling a die 3 times'''
def rollx(x):
    z=[]
    for i in range(x):
        j=equallyLikely(1, 6)
        z.append(j)
    return(sum(z))


'''simulate the rolls 100 times for distributions'''
count=[0]*19
r=[]
for i in range(10000):
    x=(rollx(5))
    r.append(x)
    for u in range(0, 19):
        if (x==u):
            count[u]+=1

'''Print the average'''
print("Average Roll: ", sum(r)/len(r))
print(count)

for n in range(19):
    print("Odds of rolling a ", n, ": ", count[n]/len(r))


    

    
