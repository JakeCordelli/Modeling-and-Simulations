import random

x=random.randrange(0, 2)

print(x)


zeroCount=0
oneCount=0

if(x==0):
    zeroCount=zeroCount+1


if (x==1):
    oneCount+=1


print("oneCount", oneCount)
print("zeroCount", zeroCount)
#print("Ratio 1:0 ", oneCount/zeroCount)
