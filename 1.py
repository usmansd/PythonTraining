#pairs_1=[]
#for num1 in range(0,2):
#    for num2 in range(6,8):
#        pairs_1(num1,num2)
#print(pairs_1)

'''
result =(num for num in range (6))

for num in result:
    print(num)

result =[num for num in range(10**3)]

print(list(result))

print('hello world')

# list comprehension with square bracket.
even_num = [num for num in range(0,10) if num % 2==0]
print(even_num)

# list generator with rount bracket.
even_num = (num for num in range(0,10) if num % 2==0)

print(list(even_num))

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])


mean= np.array ([np_height,np_weight])
#print(mean)

for val in np.nditer(mean):
    print(mean)

def square(value):
    new_value=value**2
    return (new_value)

print(square(4))

def raisepower(value1,value2):
    new_value1= value1**value2
    new_value2=value2**value1
    new_value=(new_value1,new_value2)
    return new_value

print(raisepower(2,3))


def mod2plus5(x1,x2,x3):
    def inner(x):
        return x%2+5
    return (inner(x1),inner(x2),inner(x3))

print(mod2plus5(3,4,5))



nums = [12, 8, 21, 3, 16]

new_num =[]

for num in nums:
    new_num.append(num+1)

print(new_num)


new_num2 =[num+1 for num in nums]

print(new_num2)

a=[num for num in range(11)]
print(a)
'''

pairs_1 = []

for num1 in range(0,2):
    for num2 in range(6,8):
        pairs_1.append(num1,num2)

#print(pairs_1)

pairs_2 = [(num1,num2) for num1 in range(0,2) for num2 in range (6,8)]
