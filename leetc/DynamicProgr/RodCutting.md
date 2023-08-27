
``` Python

prices = [1,5,8,9,10,17,17,20]

def rod_cutting(prices):

    values = [0 for val in range(len(prices)+1)]
    length = len(prices)  
    
    for val in range(1,len(prices)+1):
        profit = prices[val-1]
        for valtwo in range(1,val):
            option = prices[valtwo-1] + values[val-valtwo]
            profit = max(profit,option)

        values[val]=profit

    return values[-1]
```
