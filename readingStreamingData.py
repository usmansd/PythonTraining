"""
reading streaming data or the file line by line.

Processing data in chunks (1)
Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive.
 In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of
 how many times each country appears in a column in the dataset.

The csv file 'world_dev_ind.csv' is in your current directory for your use. To begin, you need to open a connection to
this file using what is known as a context manager. For example, the command with open('datacamp.csv') as datacamp binds
the csv file 'datacamp.csv' as datacamp in the context manager. Here, the with statement is the context manager, and
its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.

If you'd like to learn more about context managers, refer to the DataCamp course on Importing Data in Python.

Instructions
100 XP
Use open() to bind the csv file 'world_dev_ind.csv' as file in the context manager.
Complete the for loop so that it iterates 1000 times to perform the loop body and process only the first 1000 rows of
data of the file.

"""
#Open a connection to the file
with open('tweets.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        # converting the row into a list so that we can use slicer
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

"""
Writing a generator to load data in chunks (2)
In the previous exercise, you processed a file line by line for a given number of lines. What if, however,
you want to do this for the entire file?

In this case, it would be useful to use generators. Generators allow users to lazily evaluate data. This concept of lazy
evaluation is useful when you have to deal with very large data sets because it lets you generate values in an efficient 
manner by yielding only chunks of data at a time instead of the whole thing at once.

In this exercise, you will define a generator function read_large_file() that produces a generator object which yields 
a single line from a file each time next() is called on it. The csv file 'world_dev_ind.csv' is in your current 
directory for your use.

Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, 
you won't have to explicitly create generator objects in cases such as this. However, for pedagogical reasons, we are 
having you practice how to do this here with the read_large_file() function. Go for it!

Instructions
100 XP
In the function read_large_file(), read a line from file_object by using the method readline(). Assign the result to data.
In the function read_large_file(), yield the line read from the file data.
In the context manager, create a generator object gen_file by calling your generator function read_large_file() and 
passing file to it.
Print the first three lines produced by the generator object gen_file using next().
"""


# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data


# Open a connection to the file
with open('world_dev_ind.csv') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))


"""
Writing a generator to load data in chunks (3)
Great! You've just created a generator function that you can use to help you process large files.

Now let's use your generator function to process the World Bank dataset like you did previously. You will process the 
file line by line, to create a dictionary of the counts of how many times each country appears in a column in the 
dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use. 
Go for it!

Instructions
100 XP
Bind the file 'world_dev_ind.csv' to file in the context manager with open().
Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all 
the rows of the file.
"""

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
print(counts_dict)