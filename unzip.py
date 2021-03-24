"""
Using * and zip to 'unzip'
You know how to use zip() as well as how to print out values from a zip object. Excellent!

Let's play around with zip() a little more. There is no unzip function for doing the reverse of what zip() does.
We can, however, reverse what has been zipped together by using zip() with a little help from *! *
 unpacks an iterable such as a list or a tuple into positional arguments in a function call.

In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().

Two tuples of strings, mutants and powers have been pre-loaded.
"""

mutants =['charles xavier','bobby drake','kurt wagner','max eisenhardt','kitty pryde']
powers =['telepathy','thermokinesis','teleportation','magnetokinesis','intangibility']

z1= zip(mutants,powers)
#print(z1)
print(list(z1))

print('---------------------------------')

z1=zip(mutants,powers)
result1, result2 = zip(*z1)
print (result1)
print (result2)
