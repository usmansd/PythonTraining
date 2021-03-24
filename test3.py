'''
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'cars_per_cap': cpc, 'country': names, 'drives_right': dr}
for i in iter(cars_dict):
    print(i)
'''




def raise_val(n):

    def inner(x):
        raised = x**n
        return raised
    return inner

cube= raise_val(3)

print(cube(5))