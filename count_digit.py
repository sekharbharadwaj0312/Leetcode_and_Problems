def countdgt(i,u,x):
    count = 0

    for num in range(i, u+1):
        num_str = str(num)

        count += num_str.count(str(x))

    return count

i = int(input())
u = int(input())
x = int(input())

result = countdgt(i,u,x)
print(result)