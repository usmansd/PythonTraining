"""
Reduce() and lambda functions
You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills.
The reduce() function is useful for performing some computation on a list and, unlike map() and filter(),
returns a single value as a result. To use reduce(), you must import it from the functools module.
"""
"""
Remember gibberish() from a few exercises back?
# Define gibberish
def gibberish(*args):
    #Concatenate strings in *args together
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge
"""
"""
gibberish() simply takes a list of strings as an argument and returns, as a single-value result,
the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and
a lambda function that concatenates strings together.
"""

from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda item1, item2 : item1 + item2 , stark)
print(result)



