#adapted from code from Dr. Kastner

#In-Class Example
import math
import time  

fileName = "CocaColaVolume"
maxVal = -10000000.0
minVal = 10000000.0
maxBin = 0

#Inputs
fid = open(fileName + ".txt","r")
x_list = fid.readlines()
fid.close()
for i in range(len(x_list)):
    x_list[i] = float(x_list[i])
    if x_list[i] > maxVal:
        maxVal = x_list[i]
    if x_list[i] < minVal:
        minVal = x_list[i]


#Analysis
n = len(x_list)
num = 1 + 3.322 * (math.log10(n))
num = int(math.ceil(num))
interval = (maxVal - minVal) / num
Bin = [0]*num
top = [0]*num
bottom = [0]*num
row = [0]*(2 + num)

i = -1

while top[i] < maxVal:
    i = i + 1
    bottom[i] = minVal + (i * interval)
    top[i] = minVal + ((i + 1) * interval)
    #print(bottom[i])
    #print(top[i])
    for k in range(n):
        if x_list[k] >= bottom[i] and x_list[k] < top[i]:
            Bin[i] = Bin[i] + 1
Bin[len(Bin) - 1] = Bin[len(Bin) - 1] + 1

#Print Bin Data
for k in range(num):
    b = k + 1
    print('Bin {0} = {1}'.format(b,Bin[k]))
    if Bin[k] > maxBin:
        maxBin = Bin[k]

print(" \n")
print(fileName + " Distribution\n")

#Indexing and Printing Histogram
for i in range(maxBin, -1, -1):
    row[0] = i + 1
    row[1] = " |"
    for k in range(num):
        if Bin[k] >= i + 1:
            row[k+2] = "|//|"
        elif  Bin[k] == i:
            row[k+2] = " __ "
        else:
            row[k+2] = "    "
    if row[0] >= 10:
        row[1] = "|"
    
    for j in range(num + 2):
        print("{0}".format(row[j]), end="", flush=True)
        time.sleep(0.015)
    print("\n", end="", flush=True)

for k in range(num * 4 + 3):
    print("‾", end="", flush=True)
print("\n")
