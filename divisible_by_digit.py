def is_divisible_by_digit_operations(num):

    digits = [int(digit) for digit in str(num)]
    if 0 in digits:
        return False
    sum_of_digits = sum(digits)

    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit

    return num % sum_of_digits == 0 or num % product_of_digits == 0

def count_divisible_elements(arr):
    count = 0
    for num in arr:
        if is_divisible_by_digit_operations(num):
            count += 1
    return count

array_length = int(input())
arr = []
for _ in range(array_length):
    num = int(input())
    arr.append(num)

result = count_divisible_elements(arr)
print(result)
