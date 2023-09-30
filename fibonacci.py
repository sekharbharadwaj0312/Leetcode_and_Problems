num1, num2 = 0, 1
n = int(input())
print("Fibonacci sequence:")

for i in range(n):
    
    print(num1, end="  ")
    
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res