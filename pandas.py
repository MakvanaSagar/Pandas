
-> Pandas is a Python library used for working with data sets.

-> pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool

-> It has functions for analyzing, cleaning, exploring, and manipulating data.

-> Pandas can clean messy data sets, and make them readable and relevant.
"""

import pandas as pd

x = [1,4,2]
y = pd.Series(x, index = ['a','b','c'])
print(y)

#If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.





data = {
    "Day":[23,24,25],
    "Weight":[78,77,74]
}

z = pd.DataFrame(data)
print(z)

print()

d = pd.DataFrame(data, index = ['Day1','Day2','Day3'])
print(d)

#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.





import pandas as pd

df = pd.read_csv("AAPL_historical_data.csv")
print(df)

#A simple way to store big data sets is to use CSV files (comma separated files).






df = pd.read_csv("AAPL_historical_data.csv")
print(df.to_string)




df = pd.read_csv("AAPL_historical_data.csv")
print(df.dropna)

#Remove all rows wit NULL values from the DataFrame.




df = pd.read_csv("AAPL_historical_data.csv")
x = df.drop(11093)
print(x)

#The drop() method removes the specified row or column.





df = pd.read_csv("AAPL_historical_data.csv")
x = df.duplicated()
print(x)

#The duplicated() method returns a Series with True and False values that describe which rows in the DataFrame are duplicated and not.