for i in range(n+1):
    for j in range(n):
        if j<=n-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
