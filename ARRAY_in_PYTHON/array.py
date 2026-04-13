from array import *
val = array('i',[1,2,3,4,5,6])

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print('\n')


# for x in val:

#     print(x, end=",")
# print('\n')

# print(val.typecode)

# val.reverse()
# for i in range(0,len(val)):
#     print(val[i], end=" ")



# val.insert(0,50)
# val.append(100)
# val[3] = 44

copyArray = array(val.typecode, (x*2 for x in val))

# copyArray.pop(3)
# copyArray.remove(12)
SA = val[0 : 3]


for i in range(0,len(SA)):
    print(SA[i], end=" ")

