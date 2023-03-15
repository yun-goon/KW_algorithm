import random
from timeit import default_timer as timer

def bubble_sort(A):
    for last in range (len(A)-1, 0, -1):
        sorted = True
        for i in range(last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False
        if sorted:
            break

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
x.sort(reverse= True)
start = timer()
bubble_sort(x)
print(timer() - start)
print(x)
print(test(x))