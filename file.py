
import pandas as pd
data = pd.read_csv("data/usdrub_d.csv")

#
# data.query('Date')
def calc_poor_ratio(price, year):
    coefficient_year = data[data['Date'].str.contains(year)]['Close'].mean()
    coefficient_2022 = data.iloc[-1]['Close']
    ratio = coefficient_2022 / coefficient_year
    return ratio

test_year = '2021'
test_price = 15000
r = calc_poor_ratio(test_price, test_year)
print(r)

"""
TODO
1. How to import "*.py" files in python Anna: if the file in the same directory, you can just import 'name of the file'
2. How to call a function defined in other file. (function is separated from its usage) Anna: you can use from 'name of the file' import 'function'
3. Where python looks for files when you try to import something. Anna: I guess it searches through the directory, and it can only find it if its in the same directory. To find the file in a different folder, we need to indicate the entire path to it. For example, ./name of the folder/ name of the file.
4. What happens when python imports a file. Anna: It employs the function of that file?
5. Should you delete lines 13-16 or move to separate file (eg test_poor_ratio.py), or 
   should you keep them? Anna: It doesnt seem like a necessary action to move them to a different file
"""