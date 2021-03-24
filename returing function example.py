"""
nums=[12,8,21,3,16]
new_nums= [a + 1 for a in nums]
print(new_nums)

a=12345
b='12345'

print(type(a))
print(type(b))
import numpy as np
list1=np.array([0,1,2,3,4,5,6,7,8,9])
for i in list1:
    a= np.array(i**2)
    print(a)
print(type(a))

result = [num for num in range(11)]
print (result)

pairs_1=[]

for num1 in range (0,6):
    for num2 in range (7,12):
        pairs_1.append(num1, num2)
print(pairs_1)

"""
square = []

for i in range(0,10):
    a= i**2
    print(a)
