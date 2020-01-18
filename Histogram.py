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
    
Bin = [0, 0, 0, 0, 0, 0, 0]

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
    elif x_list[k] <= 1.038:
        Bin[5] = Bin[5] + 1

row = [0]*8

for k in range(6):
    b = k + 1
    print('Bin {0} = {1}'.format(b,Bin[k]))

print(" \n")

for i in range(9, -1, -1):
    row[0] = i + 1
    for k in range(6):
        if Bin[k] >= i + 1:
            row[k+1] = "|//|"
        elif  Bin[k] == i:
            row[k+1] = " __ "
        else:
            row[k+1] = "    "
    time.sleep(0.05)
    if i == 9:
        row[2] = "   "
    print("{0}  {1}{2}{3}{4}{5}{6}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
print("\n")
