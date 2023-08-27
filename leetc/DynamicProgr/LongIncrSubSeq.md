
Code:

~~~Python 
    def lengthOfLIS(nums):
        array = [1 for val in range(len(nums))]
        for outer_index in range(len(nums)):
            for inner_index in range(outer_index):
	            outer_number = nums[outer_index]
	            inner_number = nums[inner_index]
                if inner_number<outer_number:

                    array[outer_index] =\
              max(array[outer_index],array[inner_index]+1)
        return max(array)

~~~

Base case: array of length 1. Longest subsequence is obviously 1.

For any array of length greater than 1, we have essentially two scenarios when comparing outer_number with inner_number.

In scenario 1, inner_number is greater than or equal to outer_number. Nothing happens in this case because the subsequence is not increasing, and the inner loop iterator moves on to the next value of inner_index.

In scenario 2, inner_number is smaller than outer_number, and then within scenario 2 we have two possible nested scenarios. Either we continue the existing subsequence at array[inner_index] by incrementing it by 1 (because outer_number is now part of the subsequence) and we store array[inner_index]+1 at array[outer_index], or there was an already existing increasing subsequence that ended at outer_number but did not include inner_number, of which we already stored the length of at array[outer_index] and is a longer subsequence than this new potential increasing subsequence which is has a length of array[inner_index]+1, and therefore we do not modify the value of array[outer_index].

Proof by induction

The recurrence relation is what makes this algorithm work and is captured in this line of code: 
```Python
```max(array[outer_index],array[inner_index]+1)
```
for i,j where i <= j, dp[j] = max(dp[j], dp[i]+1)

where dp is the array that stores the length of the longest increasing subsequence at index j



Base Case (same as above): Array of length 1. Longest subsequence is obviously 1. This is trivial

1. Assume the array is optimal for N numbers. If we can show it is optimal for N+1 numbers, then using our base case as a starting point we can show that it works for any amount of numbers.
2. When we reach the N+1th index in our outer_index loop, initially, the value of array[N+1] is 1.  We then proceed to the inner iterator which traverses all index values in range(0,N+1) and calls the max operator between array[N+1] and array[inner_index]+1. There are two scenarios that can occur here. In the following steps, we define the word "optimal" to mean "storing the correct value of the longest increasing subsequence up until a particular index value in 'nums', at that specific index value in 'array'"
	1. Scenario 1 is that the array[inner_index]+1 value is greater than array[N+1], and in that case array[N+1] is set to array[inner_index]+1. The key here is that array[N+1] is taking incrementing array[inner_index] by 1 and by definition inner_index is <= N, which we assumed to be optimal. So once the inner_index loop terminates, we can be sure that we have compared every value of array[0:N] to the value of array[N+1]. Since we have assumed array[0:N] is optimal, and have made every possible comparison to array[N+1], we now know array[N+1] is optimal.
	2. Scenario 2 is that array[N+1] is greater than array[inner_index]+1, and in this case nothing happens. The key here is that in order for array[N+1] to be greater than 1, there had to have already been an existing subsequence that ended with nums[N+1] and all previous values of the subsequence are therefore also a shorter subsequence that ended at an index <= N, and was incremented by including the nums[N+1] value. 
	3. Therefore in both cases, in order for array[N+1] to be greater than 1, it has to be a continuation of a shorter subsequence who's final index value in array was <= N, which is are assuming to be optimal
3. Therefore, if we start with 1 number as our base case, we've proven it's optimal for 2 numbers. Then we use 2 numbers as our base case, and we know it's optimal for 3 numbers, and so on and so forth.









