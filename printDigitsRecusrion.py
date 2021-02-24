def fun(n):
    if n < 10:
        return n
    else:
        fun(int(n/10))
        return "; "+str(n%10)


print(fun(101))