#importing array
import array as arr

'''#creation of array
a1=arr.array('i', [1,2,3,4,5])
a2=arr.array('d',[2.3,2.1,5.0,8.99,2.1])
a3=arr.array('u',['a','b','n','s'])

#type codes

print(a1.typecode)
print(a2.typecode)
print(a3.typecode)

#firstlookatarray
print(len(a1))

#using for accessing

for i in range(0,len(a1)):
    print(a1[i],end='')
print('\n')

#adding array usig list
x=list(range(1,100,2))
new_arr=arr.array('i',x)

for i in range(0,len(new_arr)):
    print(new_arr[i],end=' ')
print('/n')
print(new_arr[15])

##nxt
a4=arr.array('i',[8,9,5,4])
for i in range(0,len(a4)):
    print(a4[i],end=" ")
print("/n")

a1.insert(5,6)
a1.insert(6,7)
a1.insert(7,6)
print(a1)
a1.append(8)
for i in range(0,len(a1)):
    print(a1[i],end=' ')
a1[7]=8
a1[8]=9
print('/n')
for i in range(0,len(a1)):
    print(a1[i],end='')
print("/n")

#delete

a1.pop(3)
for i in range(0,len(a1)):
    print(a1[i],end=' ')
print("/n")'''

#slicing

'''x=list(range(0,100,2))
p2=arr.array('i',x)
for i in range(0,len(p2)):
    print(p2[i],end=' ')
print('/n')

arr5=p2[-1:-50:-1]
for i in range(0,len(arr5)):
    print(arr5[i],end=' ')
print('/n')

arr6=p2[::-1]
for i in range(0,len(arr6)):
    print(arr6[i],end=" ")
print("/n")

'''

'''#searchig operations

x=list(range(1,10000000,2))
cc=arr.array('i',x)

for i in range(0,len(cc[0:10])):
    print(cc[i],end=' ')
print("/n")

index=cc.index(1201)
res=cc[index]
print(index,res)

#sorting operations

arx=arr.array('i',[5,3,6,1,8,0])
ary=arx.tolist()

ary.sort()
print(ary)

ary.sort(reverse=True)
print(ary)'''

#Numpy array

import numpy as  np
arr=np.array([1,2,3,4,5])
print(arr)

zeros=np.zeros((2,2))
print(zeros)

ones=np.ones((3,3))
print(ones)

const=np.full((2,2),0)
print(const)

ident=np.eye(7)
print(ident)

ran=np.random.random((3,2))
print(ran)

#0d
zerod=np.array(1)
print(zerod)

#1d
oned=np.array([1,2])
print(oned)

#2d
twod=np.array([[1,3,5,7],[9,5,3,1]])
print(twod)

#3d
threed=np.array([[[1,2,3],[4,5,6]],[[12,13,14],[15,6,17]]])
print(threed)