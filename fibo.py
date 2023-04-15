def FIB(n):
    f = [0] * (n+1)
    if f[n] != 0:
        return f[n]
    if n ==1 or n==2:
        f[n] = 1
    else:
        f[n] = FIB(n-1) + FIB(n-2)
    return f[n]

a = FIB(6)

print(a,"\n")
