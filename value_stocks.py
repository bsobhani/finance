import pandas as pd
import numpy as np
financials = pd.read_csv("financials_with_price_2013.csv")
print(financials[["stock", "stockholdersequity", "earningspersharebasic", "commonstocksharesissued"]])
def calculate_book_value_row(row):
	equity = row["stockholdersequity"]
	num_shares = row["commonstocksharesissued"]
	return equity/num_shares
def calculate_value_row(row):
	#equity = row["stockholdersequity"]
	eps = row["earningspersharebasic"]
	#num_shares = row["commonstocksharesissued"]
	
	#book_value = 0*equity/num_shares
	book_value = calculate_book_value_row(row)
	#income_value = 4*eps/.07
	income_value = 4*eps/.05
	value = book_value + income_value
	return value



financials = financials.dropna(subset=["price"])
#for index, row in financials.iterrows():
#	val = calculate_value_row(row)
#	price = row["price"]
#	print(val, price, price/val, row["stock"], row["filing_date"])
financials["bv"] = calculate_book_value_row(financials)
financials["value"] = calculate_value_row(financials)
financials["pv"] = financials["price"]/financials["value"]
financials = financials.dropna(subset=["pv"])
financials = financials[financials.pv>0]
financials = financials[financials.bv<financials.price*10]
financials = financials[financials.earningspersharebasic<financials.price*10]
#cols = ["stock", "stockholdersequity", "earningspersharebasic", "commonstocksharesissued", "price", "pv"]
cols = ["stock", "bv", "earningspersharebasic", "commonstocksharesissued", "price", "pv"]
print(financials[cols].sort_values(by=["pv"]).head(50))
