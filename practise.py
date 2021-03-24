
'''
age=18

while age<50 :

    print("not old enough current age is " ,  age );
    age +=1


""""
you type for and then you would type a 
temporary name we'll call it item 
and then use the keyword in and you specify 
your list and then a colon
so in here it's gonna run whatever code
you write now it's gonna run it in my
case it's gonna run it what six times
actually yeah six times so what I'll do
is I'll simply just print out the item
"""
my_list= [1,2,3,4,5,"usman",True]

for item in my_list:
    print (item)


#dictionary

my_dict= {}

my_dict['name']='usman'
my_dict['state']='ontario'
my_dict['age']='32'

#print(my_dict)
#iteration over dictionary

for k,v in my_dict.items():
    print (k,'=>',v)


#functions

def add(n1, n2) :
    return n1+n2

print (add(1, 2 ))


def square(n1, n2 ):
    return n1**2, n2**2


result1 , result2= square(1,2)
print ( result1 , result2)


class Person:
    name=None
    age=None

    def say_name(self):
        print('my name is %s' % self.name)
    def say_age(selfself):
        print('my name is %d' % selfself.age)

'''



#place holders
message= 'hello world'
name='usman'
a=message+name

print(message.replace('world', 'universe'))
print(a)

b= '{},{}'.format(message,name)

print(b)

#f string
message='hello world'
name='usman'
a= f'{message},{name}'
print(a)
