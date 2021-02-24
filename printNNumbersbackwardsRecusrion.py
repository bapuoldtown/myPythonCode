def function(n):
    if n == 0:
        return
    else:
        print(n,end=" ")
        function(n-1)

function(3)