import random
from timeit import default_timer as timer

def insertion_sort(A):
    for i in range(1, len(A)):
        loc = i -1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newItem

def test(A):
	for i in range(1,len(A)):
		if A[i-1] > A[i]:
			return False
	return True

data = random.sample(range(10000), 100)
start = timer()
insertion_sort(data)
print(timer() - start)
print(data)
print(test(data))