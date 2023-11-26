num =int(input())
sum1=0 
num_new = list(str(num))
for i in num_new :
    i = int(i)
    sum1 = sum1 + (i*i*i)
if sum1 == num :
    print("The entered number is amstrong number")
else: 
    print("The entered number is not the amstrong number")
