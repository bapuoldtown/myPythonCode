def printArrayRecursively(arr,n):
    if n == 1:
        print(arr[0])
        return
    else:
        printArrayRecursively(arr,n-1)
        print(arr[n-1])

printArrayRecursively([1,2,3,4,5],5)

    

