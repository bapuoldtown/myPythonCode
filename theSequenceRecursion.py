def theSequence(n):
    if n == 0:
        return 1
    else:
        return n+n*theSequence(n-1)

print(theSequence(2))
print(theSequence(3))
