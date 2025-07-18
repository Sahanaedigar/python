def bestDayToBuyStocks(prices):
    buyingprice=min(prices)
    maxprofit=0
    print(buyingprice)
    lengthofthe_array=len(prices)

    for i in range(1,lengthofthe_array):
        profit=prices[i]-buyingprice
        if profit>maxprofit:
            maxprofit=profit
    return maxprofit

prices=[7,1,5,3,6,4,17]
print(bestDayToBuyStocks(prices))

'''
we cannot sell the stocks in the prious day 
for ex if we are buying on day one(idex=1) cannot seel it on the index 0 i.e previous day hence
 we are neglecting 1st day we cannot do any thing in day one'''