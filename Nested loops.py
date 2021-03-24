"""
Nested Functions I
You've learned in the last video about nesting functions within functions. One reason why you'd like to do this is to
avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested
functions: you simply define it as you would a regular function with def and embed it inside another function!

In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string
object with !!!. three_shouts() then returns a tuple of three elements, each a string concatenated with !!!
using inner()
Go for it!

Instructions
100 XP
Complete the function header of the nested function with the function name inner() and a single parameter word.
Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters
from three_shouts() as arguments to each call.

Take Hint (-30 XP)

"""


# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return inner(word1), inner(word2), inner(word3)


# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

"""

Nested Functions II
Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions
is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope
when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when 
the outer function has finished execution.

Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then
call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!

Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
Complete the function echo() so that it returns inner_echo.
We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call 
echo(), passing 3 as an argument. Assign the resulting function to thrice.
Hit Submit to call twice() and thrice() and print the results.
"""


# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo


# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
