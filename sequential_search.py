import random
from timeit import default_timer as timer

def sequential_search(x,value):
    n = len(x)
    for i in range(n):
        if x[i] == value:
            return i
    return -1

x = random.sample(range(5000),1000)
value = x[800]
start =timer()
index = sequential_search(x,value)
print(timer() - start)

print('value', value, 'found', index)
print(True if index >= 0 and x[index] == value else False)