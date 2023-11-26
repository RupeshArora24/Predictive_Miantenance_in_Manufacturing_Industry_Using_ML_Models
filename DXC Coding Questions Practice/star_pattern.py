rows = int(input())
for i in range(0,rows+1):
    for k in range(i,rows):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,i):
        print("*",end=" ")    
    print()

