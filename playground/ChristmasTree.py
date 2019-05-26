def christmastree(n):
    for i in range(0,n):
        print (" "*(n-i) + "*"*(2*i+1))
    for j in range (0,n-1):
        print(" " * (j+2) + "*" * (2 * (n-j) - 3))


christmastree(35)