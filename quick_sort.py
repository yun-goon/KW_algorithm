import random
# A : 정리할 배열
# p : 순서
# r : 길이
def partition(A, p, r):
    x = A[r] # 하나 만듦
    i = p # 몇번째부터
    print(x,i)
    for j in range(p,r-1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i] # 자리 바꿈
    return i # i번째를 리턴시킴

'''
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
'''

def qsort(A, p, r): #재귀로 하나가 될때 까지 돎
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)

def quick_sort(A):
    qsort(A, 0, len(A)-1) # A와 0, 4가 들어갈꺼임

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)

quick_sort(x)

print(x)
print(test(x))

'''
1. 랜덤 배열 x를 생성함
2. quick_sort에 집어넣음
3. qsort를 실행함
'''