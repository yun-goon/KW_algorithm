import random


def partition(A, p, r):
    x = A[p]
    left = p+1
    right =r

    while True:
        while left <= right and A[left] <= x:
            left += 1
        while left <= right and x <= A[right]:
            right -= 1
        if right < left:
            break
        else:
            A[left],A[right] = A[right],A[left]
    A[p], A[right] = A[right], A[p]
    return right




def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q + 1, r)

def quick_sort(A):
    qsort(A, 0, len(A)-1)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)

quick_sort(x)

print(x)
print(test(x))