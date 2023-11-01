def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def SumofSetBitNumbers(n, set):
    total_sum = 0
    for i in range(2 ** n):
        if count_set_bits(i) == set:
            total_sum += i
    return total_sum

n = int(input())
set = int(input())

result = SumofSetBitNumbers(n, set)
print(result)
