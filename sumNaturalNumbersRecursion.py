"""sum of first n natiral numbets using recursion"""
ef function(n):
    if n == 1:
        return 1
    return n+function(n-1)


print(function(4))