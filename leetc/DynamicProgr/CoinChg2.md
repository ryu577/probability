~~~ Python 

def change(amount,coins):
    if amount==0:
        return 1
    if min(coins)>amount:
        return 0
    matrix = [[0 for val in range(amount+1)] for val in range(len(coins)+1)]

    for val in range(1,len(coins)+1):
        for valtwo in range(1,amount+1):
            coin = coins[val-1]
            if coin==valtwo:
                matrix[val][valtwo]= matrix[val-1][valtwo]+1
            elif coin > valtwo:
                matrix[val][valtwo]=matrix[val-1][valtwo]
            else:
                difference_needed = valtwo-coins[val-1]
                previous_row_ways = matrix[val-1][valtwo]
                num_ways = matrix[val][difference_needed]+previous_row_ways
                matrix[val][valtwo]+=num_ways      



    return matrix[-1][-1]    

~~~
#dynprogr #cs 
