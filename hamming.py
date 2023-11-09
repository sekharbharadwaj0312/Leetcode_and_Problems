def is_binary_string(s):
    return all(bit in '01' for bit in s)

def calculate_cost(s, A, B):
    count_01 = s.count('01')
    count_10 = s.count('10')
    return count_01 * A + count_10 * B

def hamming_distance(s1, s2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(s1, s2))

def minimize_cost_and_print_distance(s, A, B):
    if not is_binary_string(s):
        print("INVALID")
        return

    original_cost = calculate_cost(s, A, B)
    min_cost = original_cost
    min_hamming_distance = 0

    # Try all possible rearrangements
    for i in range(1, len(s)):
        rearranged_s = s[i:] + s[:i]
        cost = calculate_cost(rearranged_s, A, B)

        if cost < min_cost or (cost == min_cost and hamming_distance(s, rearranged_s) < min_hamming_distance):
            min_cost = cost
            min_hamming_distance = hamming_distance(s, rearranged_s)

    print(min_hamming_distance)

# Read input
T = int(input())
for _ in range(T):
    binary_string = input().strip()
    A, B = map(int, input().split())
    minimize_cost_and_print_distance(binary_string, A, B)
