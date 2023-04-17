

def pebble(n):
    for p in range(1,5):
        peb[1][p] = w[1][p]
    for i in range(n+1):
        for p in range(1,5):
            peb[i][p] = max