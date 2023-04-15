import random
from timeit import default_timer as timer

def rsort(A,m):
    buckets = [[] for _ in range(10) ]
    for v in A:
        index = v // (10 **m)
        index %= 10
        buckets[index].append(v)
    res = []
    for bucket in buckets:
        res.extend(bucket)
    return res

def radix_sort(A,k):
    for i in range(0,k):
        A = rsort(A,i)
    return A

def test(A):
    for i in range(1,len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
x = radix_sort(x,4)
print(timer() - start)
print(x)
print(test(x))