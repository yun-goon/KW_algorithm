import random
from timeit import default_timer as timer

def selection_sort(x):
	print(len(x))
	for last in range(len(x)-1, 0,-1):
		largest = 0
		print("last = ", last)
		for i  in range(1,last+1):
			print(i)
			if x[i] > x[largest]:
				largest = i
		x[largest], x[last] = x[last], x[largest]

def test(x):
	for i in range(1,len(x)):
		if x[i-1] > x[i]:
			return False
	return True

data = random.sample(range(10000), 10)
start = timer()
selection_sort(data)
print(timer() - start)
print(data)
print(test(data))
