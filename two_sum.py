l = list(map(int, input("nums: ").split(",")))
t = int(input("target: "))
# n[i] + n[j] should be equal to t; so we can run a loop through n using i, select a number, then select another number using j loop,
# and check the sum. So,take a number in i loop, go through each number in j loop, and check the sum. If we do not get the sum, we will
# have to go to the next element of i, then, we have to keep checking until we find the sum.
x = 0
m = 0
n = 0
b = False
for i in range(len(l)):
    if b == True:
        break
    for j in range(len(l)):
       x = l[i]+l[j]
       if t == x:
        b = True
        print("[",i, ",",j, "]")