stocks = {"AAPL": 180,
          "TSLA": 230,
          "MSFT": 500,
          "AMZN": 130}
shares = []
print("Enter the stock shares you have in each of the following stocks: ")
for stock in stocks:
  print(stock, end="")
  share = input()
  total = stocks[stock] * int(share)
1
print("Total invetment value is : ", total)
