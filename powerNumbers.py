def RecursivePower(n,p):
    if p == 0:
        return 1
    else:
        return n*RecursivePower(n,p-1)
print(fpower(2,4))