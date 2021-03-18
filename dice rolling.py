import random
import matplotlib.pyplot as plt
datax = []
E= 2.17
datay =[]

N0 = 1000
num1 = N0
datax.append([])
datay.append([])
num_of_full = 0
while num1>0:
    
    ind = 0
    while ind<num1:
        roll = random.randint(0,6)
        if roll == 6:
            num1-=1
        ind+=1
    datax[0].append(num_of_full)
    datay[0].append(num1)
    num_of_full+=1

plt.plot(datax[0], datay[0], label = "Continous Decay")

num_of_full=0
num2 = N0
datax.append([])
datay.append([])
while num2>1:
    num2*=5/6


    
    datay[1].append(num2)
    datax[1].append(num_of_full)
    num_of_full+=1


plt.plot(datax[1], datay[1], label = "Geometric Decay")
datax.append([])
datay.append([])
num3 = N0
t=0
while num3>1:
    num3 = N0*E**(-t/6)
    t+=1
    datax[2].append(t)
    datay[2].append(num3)

plt.plot(datax[2], datay[2], label = "Exponential Decay")
plt.xlabel("Number Of Trials")
plt.ylabel("Number Of Remaining Dice")
#plt.axis("num of total rolls")
plt.show()