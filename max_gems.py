def max_gems(n, dishes):
    dishes.sort()  # Sort dishes based on ids

    max_gems = float('-inf')

    for i in range(n):
        group = [dishes[i]]
        gems = max(group)  # Initially, consider the maximum id rating

        # Extend the group by adding dishes with consecutive ids
        for j in range(i + 1, n):
            if dishes[j][0] == group[-1][0] + 1:
                group.append(dishes[j])
                gems += max(group)  # Calculate gems by selecting the maximum id rating

        max_gems = max(max_gems, gems)

    return max_gems

# Read input
n = int(input())
dishes = [tuple(map(int, input().split(':'))) for _ in range(n)]

# Calculate and print the maximum gems
result = max_gems(n, dishes)
print(result)
