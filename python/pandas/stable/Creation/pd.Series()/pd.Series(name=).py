import pandas as pd

# Creating a Series
s = pd.Series(data=[10, 20, 30], index=['x', 'y', 'z'], dtype='int8', name='Random Name')

print(s)
'''
Output:
x    10
y    20
z    30
Name: Random Name, dtype: int8
'''