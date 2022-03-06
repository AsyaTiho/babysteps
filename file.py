
import pandas as pd
data = pd.read_csv("data/usdrub_d.csv")

#
# data.query('Date')
def calc_poor_ratio(price, year):
    ratio = 0.5
    year_rows = data[data['Date'].str.contains(year)]['Close'].mean()
    print(year_rows)
    return ratio


test_price = '10000'
test_year = '2017'
r = calc_poor_ratio(test_price, test_year)
print(r)