n=eval(input())
m=n//2
for i in range(m):
    for j in range(m-i):
        print(" ",end=(" "))
    for j in range(2*i+1):
        print("*",end=(" "))
    print()
for i in range(m+1,0,-1):
    for j in range(m+1-i,0,-1):
        print(" ",end=" ")
    for j in range(2*i-1,0,-1):
        print("*",end=" ")
    print()
