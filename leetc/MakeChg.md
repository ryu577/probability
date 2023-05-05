```python
import numpy as np


def min_chg(a=np.array([1, 2, 5])):
	sum_coins = sum(a)
	arr = np.zeros((len(a), sum_coins))
	if a[0] == 1:
		for j in range(len(a)):
			arr[j, 0] = 1
	else:
		return arr
	for j in range(1, sum_coins):
		for i in range(1, len(a)):
			if a[i] == j+1:
				for k in range(i, len(a)):
					arr[k, j] = 1
				break
			if arr[i-1, j-a[i]] == 1:
				for k in range(i, len(a)):
					arr[k, j] = 1
				break
	return arr

```

