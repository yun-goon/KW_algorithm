import random
from timeit import default_timer as timer

def merge_sort(A,p,r):
    if p < r:
        q = (p+r) // 2
        merge_sort(A,p,q)
        merge_sort(A,q+1, r)

        i, j, t = p , q+1, 0
        tmp = A[:]
        while i <= q and j <= r:
            if A[i] <= A[j]:
                tmp[t] = A[i]
                i += 1
            else:
                tmp[t] = A[j]
                j += 1
            t += 1
        while i <= q:
            tmp [t] = A[i]
            i += 1
            t += 1
        while j <= r:
            tmp[t] = A[j]
            j += 1
            t += 1
        i, t = p, 0
        while i <= r:
            A[i] = tmp[t]
            i += 1
            t += 1

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000),100)
start = timer()
merge_sort(x, 0, len(x) -1)
print(timer() - start)
print(x)
print(test(x))

