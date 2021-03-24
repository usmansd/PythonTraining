"""
Great! At this point, you have a good grasp of the basic syntax of list comprehensions.
Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within
 another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!
Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension
objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values
 0 to 4 in each row can be written as:
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
Your task is to recreate this matrix by using nested listed comprehensions.
Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists,
you simply have to supply the list comprehension as the output expression of the overall list comprehension:
[[output expression] for iterator variable in iterable]
Note that here, the output expression is itself a list comprehension.

instructions :

In the inner list comprehension - that is, the output expression of the nested list comprehension -
create a list of values from 0 to 4 using range(). Use col as the iterator variable.

In the iterable part of your nested list comprehension, use range() to count 5 rows -
that is, create a list of values from 0 to 4. Use row as the iterator variable; note that you won't
be needing this to create values in the list of lists.

from random import randint
import numpy as np

nums=[1,2,3,4,5,6]

for num in nums:
    new_nums=num+1
    print(new_nums)
"""


# Create a 5 x 5 matrix using a list of lists: matrix

matrix=[[col for col in range(0,5)]for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)

# list comprehensions with conditions examples

pairs_2 =[(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_2)
print([num**2 for num in range(10) if num % 2 == 0])
print([num**2 if num % 2 == 0 else 0 for num in range (10)])

#example 2

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# using if with for loop

new_fellowship = [ member for member in fellowship if len(member) >=7]

print(new_fellowship)

# using if-else with for loop

new_fellowship = [ member if len(member) >=7 else "" for member in fellowship]

print(new_fellowship)

# using dictionary comprehensions

new_fellowship = {member: len(member) for member in fellowship}
print(new_fellowship)

# list comprehension with square bracket.
even_num = [num for num in range(0,10) if num % 2==0]
print(even_num)

# list generator with rount bracket.
even_num = (num for num in range(0,10) if num % 2==0)

print(list(even_num))