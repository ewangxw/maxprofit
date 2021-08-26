import sys
from datetime import datetime, timedelta
time_format_str = '%H:%M'
stock_opening_time = '10:00'

# Prompt the user to input stock price as list.
while True:
    try:
        stock_prices = [float(item) for item in input('Enter stock price as list, separated by space: \n ').split()]
        break
    except ValueError:
        print ("Not a valid stock price! Please try again ...")

# Slice the price list into 2 lists at highest price item. Find the lowest price and calculate the max profit in first sliced list.
# Return the max profit and both sliced lists.
def slice_max_profit(price_list):
    high_price_position = price_list.index(max(price_list))
    first_sliced_list = price_list[0:high_price_position+1]
    low_price_position = first_sliced_list.index(min(first_sliced_list))
    max_profit = max(first_sliced_list) - min(first_sliced_list)
    high_price = max(first_sliced_list)
    low_price = min(first_sliced_list)
    second_sliced_list = price_list[high_price_position+1:]

    return max_profit, first_sliced_list, second_sliced_list

price_list = stock_prices
profit = 0
low_price  = 0
high_price = 0
buy_time_index = 0
sell_time_index = 0

# Compare the profit of each sliced stock price list and find lowest and highest trade price which produced the max profit. 
while len(price_list) > 0:
    max_profit = slice_max_profit(price_list)[0]

    if max_profit > profit :
        profit = max_profit
        high_price = max(slice_max_profit(price_list)[1])
        low_price = min(slice_max_profit(price_list)[1])
    
    price_list = slice_max_profit(price_list)[2]

# Throw out the warning if the stock price keep going down.
if profit == 0:
    sys.exit("The stock market is in a downturn, there is no profit for the trading !!!")


# Build up the index list of the lowerest and highest price.
low_price_index = [i for i, x in enumerate(stock_prices) if x == low_price]
high_price_index = [i for i, x in enumerate(stock_prices) if x == high_price]

# Compare the index of the lowest (buy) and highest (sell) price index and list the buy/sell plan for the max profit.
for buy in low_price_index:
    for sell in high_price_index:
        if buy < sell :
            buy_time = (datetime.strptime(stock_opening_time, time_format_str) + timedelta(minutes=buy+1)).strftime('%H:%M')
            sell_time = (datetime.strptime(stock_opening_time, time_format_str) + timedelta(minutes=sell+1)).strftime('%H:%M')
            print ("Buy at price A$" + str(low_price) + " @ " + str(buy_time) + " and sell it at price A$" + str(high_price) + " @ " + str(sell_time) + " for the max profit A$" + str(profit))
