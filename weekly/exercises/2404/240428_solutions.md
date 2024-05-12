1. P0: Code the mean time to sequence for some simple Markov chains and verify Ross's formula with simulation. 
	1. As a first step, imagine the sequence is just a single state.
2. P0: Re-read your writing of the story behind AUROC ([240317]). You should be able to recite the story and re-create the interpretation of the metric from scratch.
3. P0: Matrix chain multiplication: implement code that will give me the optimal way to multiply.
______________
4. P1: In the generate all permutations code, you're going to be handing the permutations to my program one at a time. My program will run a test on them and tell you when some condition is satisfied. When my program returns True, your code should stop and return that permutation. How would you implement this?



1 
~~~python
import numpy as np 


state_matrix = [[.1,.3,.2,.15,.25] for val in range(5)]

current_state = 0
last_state = None
two_states_ago = None 


sequence = [1,2,3]
n_transitions = 5000000
times = []
time = 1


for transition in range(n_transitions):
	next_state = np.random.choice([0,1,2,3,4],p=state_matrix[current_state])

	two_states_ago = last_state 
	last_state = current_state 
	current_state = next_state

	if [two_states_ago,last_state,current_state]==sequence:
		times.append(time)
		time=1
	else:
		time+=1

print(np.mean(times))



def calculate_state_formula(state_matrix,sequence):
	probability = state_matrix[sequence[0]][sequence[0]]

	for val in range(1,len(sequence)):
		probability*= state_matrix[sequence[val-1]][sequence[val]]
	return probability


print(1/calculate_state_formula(state_matrix,sequence))

~~~


3
![[matrix_mult_tree.jpg]]
~~~python
def reconstruct(left,right,m,matrices):
	if right-left == 1:
		return np.matmul(matrices[left],matrices[right])
	elif right-left == 0:
		return matrices[right]

	else:
		return np.matmul(reconstruct(left,m[left,right]-1,m,matrices),reconstruct(m[left,right],right,m,matrices))
~~~


4
~~~python
def swap(seq,i,j):
	seq[i],seq[j] = seq[j],seq[i]
	return seq

def condition(perm):
	if perm == [3,1,2]:
		return True
	return False

class Perm:
	def __init__(self,done):
		self.done = done

	def gen_permutations(self,start,arr):
		if not self.done:
			if start == len(arr)-1:
				print(arr)
				if condition(arr):
					self.done = True
					return arr.copy()


			for val in range(start,len(arr)):
				arr_new = swap(arr,start,val)
				arr = self.gen_permutations(start+1,arr_new)
				arr = swap(arr_new,start,val)

i = Perm(False)
i.gen_permutations(0,[1,2,3])
~~~

