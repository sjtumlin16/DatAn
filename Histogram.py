#In-Class Example
import math
import time
#Inputs
#x = float(input('Enter the Volume Added: '))
#x_list = eval(input('Enter Volume Added for all bottles: '))
fid = open("CocaColaVolume.txt","r")
x_list = fid.readlines()
fid.close()
for i in range(len(x_list)):
    x_list[i] = float(x_list[i])
    
num = 7
maxVal = 0
Bin = [0]*num

#Analysis
n = len(x_list)
for k in range(n):
    if x_list[k] < 0.996 :
        Bin[0] = Bin[0] + 1
    elif x_list[k] < 1.004:
        Bin[1] = Bin[1] + 1
    elif x_list[k] < 1.013:
        Bin[2] = Bin[2] + 1
    elif x_list[k] < 1.021:
        Bin[3] = Bin[3] + 1
    elif x_list[k] < 1.030:
        Bin[4] = Bin[4] + 1
    elif x_list[k] <= 1.034:
        Bin[5] = Bin[5] + 1
    elif x_list[k] <= 1.038:
        Bin[6] = Bin[6] + 1

row = [0]*8

for k in range(num):
    b = k + 1
    print('Bin {0} = {1}'.format(b,Bin[k]))
    if Bin[k] > maxVal:
        maxVal = Bin[k]

print(" \n")

for i in range(maxVal, -1, -1):
    row[0] = i + 1
    for k in range(num):
        if Bin[k] >= i + 1:
            row[k+1] = "|//|"
        elif  Bin[k] == i:
            row[k+1] = " __ "
        else:
            row[k+1] = "    "
    if row[0] >= 10:
        row[2] = "   "
    
    for j in range(num + 1):
        print("{0}".format(row[j]), end="", flush=True)
        time.sleep(0.015)
    print("\n", end="", flush=True)
print("\n")
