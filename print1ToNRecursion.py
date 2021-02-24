def function(n):
    if n == 0:
        return
    else:
        function(n-1)
        print(n,end="")

function(64)