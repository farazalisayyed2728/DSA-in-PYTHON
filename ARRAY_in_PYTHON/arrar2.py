from array import *

arr = array('i', [] )

n = int(input("Enter your number : "))

for i in range(0,n):
    arr.append(int(input("Enter next number : ")))

for x in arr:
    print(x , end=" ")
