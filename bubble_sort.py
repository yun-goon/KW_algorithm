import random
from timeit import default_timer as timer

def bubble_sort(A):
    for last in range(len(A) - 1, 0, -1):
        for i in range(0, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

def test(x):
	for i in range(1,len(x)):
		if x[i-1] > x[i]:
			return False
	return True

data = random.sample(range(10000), 100)
start = timer()
bubble_sort(data)
print(timer() - start)
print(data)
print(test(data))