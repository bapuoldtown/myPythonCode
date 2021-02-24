def fadd(a,b):
    if b == 0:
        return a
    else:
        return fadd(a+1,b-1)

print(fadd(2,3))