# Exercise 1
import math
result_1 = 20*math.log(5)

# Exercise 2
result_2 = (100*1.05)/(200*math.sqrt(20))

# Exercise 3
typearg = type('This is a string')

# Exercise 4
list_1 = [2,4,10,'A']

# Exercise 5
list_1_subset = list_1[0:3]

# Exercise 6
set_list = set([0.01,0.01,0.02,0.03])

# Exercise 7
continents = ['Europe','Africa','Asia']

# Exercise 8
continents_lowercase = [cont.lower() for cont in continents]

# Exercise 9
basket_groceries = {
    'apple': 1,
    'cookies': 2,
    'fish': 200
}
    
# Exercise 10
total_basket = 0 
for item in basket_groceries.values():
    total_basket += item
    

# Exercise 11
def retrieve_letters(string, character):
    result = []
    for s in string:
        if s == character:
            result.append(s)
    
    return result
    
# Exercise 12
def only_evens(input_list):
    output_list = []
    for el in input_list:
        if type(el) is str:
            return 'Invalid list!'
        elif el % 2 == 0:
            output_list.append(el)
        else: 
            pass
    return output_list
  
# Exercise 13
import numpy as np
np_zero_array = np.zeros(7)

# Exercise 14
matrix_example = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Exercise 15
first_row = matrix_example[0,:]
  
# Exercise 16
wba_data = pd.read_csv('/content/data/WBA_data.csv')

# Exercise 17
wba_data.head(10)

# Exercise 18
wba_data.tail(10)

# Exercise 19
wba_data['year'] = pd.to_datetime(wba_data.date).dt.year

# Exercise 20
wba_2014 = wba_data.loc[wba_data.year==2014]

# Exercise 21
wba_agg = wba_data.groupby(['year'])['open'].mean()