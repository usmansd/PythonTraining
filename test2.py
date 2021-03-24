import numpy as np
np.random.seed(123)

'''
outcomes=[]

for x in range(10):
    coin=np.random.randint(0,2)
    if coin == 0:
        outcomes.append("head")
    else:
        outcomes.append("tail")
print(outcomes)


tails=[0]

for x in range(10):
    coin=np.random.randint(0,2)
    tails.append(tails[x]+coin)

print(tails)



def echo( n ):
    def inner_echo(word1):

        echo_word = word1*n
        return echo_word

    return (inner_echo)

a = echo(2)
b = echo(3)

print(a('usman'))
print(b('nauman'))




def echo_shout(word):
    echo_word = word + word
    print(echo_word)

    # inner loop
    def shout():
        nonlocal echo_word
        echo_word = echo_word + '!!!'
        shout()

        print(echo_word)

echo_shout('hello')

'''
'''
import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

def count_entries(df, *args):
    cols_count = {}

    for col_name in args:

        col = df[col_name]

        for entry in col:
            if entry in cols_count.key():
                cols_count += 1

            else:
                cols_count = 1

        return cols_count

result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang', 'source')

print(result1)
print(result2)
'''

"""
#a = {1: 'math', 2: 'english', 3: 'science'}

#print((a.keys()))
#print(list(a.keys())[0])

#print(list(a.keys())[0])
#print(list(a.keys())[0])

#b = [1, 2, 3, 4, 5, 6, 7, 8]
#print(b)
#a.popitem()
#print(a)


b= [1,2 ,3, 4, 5, 6, 7]
import numpy as np
import pandas as pd
c = np.array(b)
d = pd.DataFrame(b)

i = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

d.index = i
print('##########')

print(b)
print(type(b))

print('##########')

print(c)
print(type(c))

print('##########')

print(d)
print(type(d))

print('##########')

h = np.linspace(1, 2, 10)
print(h)

help(np.linspace)
"""
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'cars_per_cap':cpc, 'country':names, 'drives_right':dr }

cars_df = pd.DataFrame(cars_dict)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars_df.index = row_labels
print(cars_df)
print(type(cars_df))

print('*******this is an object due to one []**********')
print(cars_df['country'])
print('*******this is an object due to 2 [[]]**********')
print(cars_df[['country']])
print('*******picking 2 columns**********')
print(cars_df[['country', 'drives_right']])

print('*******simple slicing in panda df, note that columns are only selected by integer**********')
print(cars_df[1:4]['country'])
print(cars_df[1:4][:])

print('*******using loc**********')

print(cars_df.loc[['AUS','JPN','US'],['country','cars_per_cap']])

print('*******using loc**********')

print(cars_df.loc[ : ,['country','cars_per_cap']])

print('*******using iloc**********')

print(cars_df.iloc[[1, 2],[1, 2]])

print(cars_df.iloc[ :,[1, 2]])


print(cars_df.iloc[1:4,1:3])
for i in cars_dict.keys():
    print(i)