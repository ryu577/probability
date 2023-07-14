amount = change amount we want to make
dp = array of length amount+1
N = number of coins
k = index value of dp array

~~~Python 

    def coinChange(coins, amount):        
        1 dp=[math.inf] * (amount+1)
        2 dp[0]=0
        
      3   for coin in coins:
        4    for k in range(coin, amount+1):
        5        if k-coin>=0:
        6            dp[k]=min(dp[k], dp[k-coin]+1)
        
        7 return dp[-1]
```
~~~


PART 1: Base case: prove it works for N = 1 coin.

1. 0th index of dp array is always 0 as per line 2 in the code. and all other indices are intialized to infinity from line 1 in the code but subject to change as the loop iterates. This is a key starting point.

2. As per line 4, we loop through each index value k of dp array, each of which represent an amount of change to be made, and if k minus the 1 coin we have is greater than or equal to zero (line 5), we proceed with the algorithm's logic
3. As you notice in line 4, the inner loop starts at the coin value. This first iteration of the inner loop is the first time any value in dp is changed from infinity. dp[k-coin] accesses the 0th index which is always 0, and the +1 increments it by 1. So dp[coin] goes from infinity to 1.

4. For all index values of dp array that are not multiples of our only coin and are not the 0th index, the algorithm takes the minimum of infinity and infinity+1 because dp[k-coin] lands on a value with is infinity, so the values stay at infinity. For all index values of dp array that ARE multiples of our only coin, if we designate the multiplier to be M, then dp[M * coin value] goes from infinity to dp[(M-1) * coin value]+1
5. If the last index value of the array is infinity, the change cannot be made. Otherwise, the last index value of the array represents the minimum amount of change to make that amount.

  
PART 2: prove it works for any number of coins

1. We need to use induction because if we show it works for 3 coins, one could always argue that maybe it doesn't work for 4 coins. We need to show that it works for any number of coins by creating a recurrence relatio.
2. Let's assume the array is optimal for N coins, for all index values. We will refer to this as N optimal for the entire array
3. If we can show that the array is optimal for N+1 coins for all index values of the array, then we can set N = 1, which would mean it works for N+1 = 2, and then we could keep traversing our way up the indices starting with this base case of N=1.
4. When we add the N+1th coin, for all index values from 1 to k = N+1th coin value -1, nothing changes because the new coin value is greater than the index value, and we already assumed it is N optimal for all index values in the array. 
5. By default, adding the N+1th coin is optimal for dp[n+1th coin value] because it obviously takes 1 coin to make the n+1th coin value - the n+1th coin itself. Therefore, we can say that the array is N+1 coins optimal for dp array index values 1 to k = N+1th coin value.
6. Now all that remains is to prove that it is N+1 optimal for ALL index values in the DP array
7. To do this, we need to use nested induction on the indices of the array. Let's assume that the array is N+1 coins optimal for the first k index values. If we can show that it is optimal for the first k+1 index values, then since we already know that it has to be N+1 optimal for the index value equal to the N+1th coin, and it is N+1 optimal for any index value that is less than the value of the N+1th coin, we can use the base case of the kth index value equaling the N+1th coin value, and use a recurrence relation to traverse all the way to the end of the array.
8. As we traverse the array from the K+1th index to the end of the array, there are two important cases. In case 1, the easier case, we DO NOT use the N+1th coin. For example if the N+1th coin is equal to 14, and we are passing through the 15th index of the dp array, if in the first N coins we already had a 15, we clearly would not need to use the new 14 value because using 1 coin is the best one can do for any index value. So since the 15th index was optimal for N coins, it is now obviously optimal for N+1 coins because we didn't use the N+1th coin.
9. In case 2, we use the N+1th coin. For any index value in the dp array which is greater than the N+1th coin, k-coin (from line in algorithm) will be an index value that is greater than 0 and less than the N+1th coin value. We already showed above that the array is N+1 optimal for all values less than or equal to k = N+1th coin value. All we're doing is taking the optimal value of the difference and incrementing it by 1.
10. We have now covered all the required cases. We first showed the array is optimal for 1 coin. We then assumed it is optimal for N coins and used induction to show it is optimal for N+1 coins. Then we simply plug in 1 coin for N, and we have proved it works for 2 coins. Then we plug in 2 coins for N, and we have proved it works for 3 coins. We have proven that the array is optimal for any number of coins.
