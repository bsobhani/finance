import pandas as pd
import numpy as np
financials = pd.read_csv("quarterly_financials.csv")
financials = financials[(financials.filing_date < "2014-01-01") & (financials.filing_date >= "2013-01-01")]
prices = pd.read_csv("all_stocks_5yr.csv")

def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))

def add_prices_to_financials(financials, prices):
	financials = financials.copy()
	#financials["price"] = ""
	#financials.insert(column="price")
	#financials = financials.assign(price=np.nan)
	financials["price"] = ""
	price_dates = prices.date
	price_dates = pd.to_datetime(price_dates)
	financial_dates = financials.filing_date
	financial_dates = pd.to_datetime(financial_dates)
	financials.filing_date = financial_dates
	prices.date = price_dates
	for index, row in financials.iterrows():
		print(index)
		ticker = row["stock"]
		date = row["filing_date"]
		#price_row = prices[prices.Name == ticker]
		#price_row = price_row[prices.date == date]
		price_dates = prices[prices.Name == ticker].date
		if len(price_dates) == 0:
			continue

		#print(nearest(price_dates, date), date)

		
		price_row = prices[(prices.date == date) & (prices.Name == ticker)]
		price = price_row["close"]
		if len(price) == 0:
			continue
		else:
			price = price.squeeze()
		#financials.loc[index] = price
		#print(financials.loc[index])
		#print(financials.loc[index].loc["price"])
		#print(financials.loc[index, "price"])
		print(type(financials))
		financials.loc[index, "price"] = price
		print(price)
		#financials.loc[index, "price"] = 7
		#print(financials.loc[index].price, price)
		print(financials.loc[index, "price"], price)
	return financials

financials = add_prices_to_financials(financials, prices)
financials.to_csv("financials_with_price.csv")

#print(financials[(financials.filing_date < "2014-01-01") & (financials.filing_date >= "2013-01-01")])
#print(financials.columns)
#for index, row in financials.iterrows():
#	print(calculate_value_row(row))

