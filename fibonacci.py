def FIB(n):
    f[1] = f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(FIB(4))