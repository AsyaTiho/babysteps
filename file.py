
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