#Knapsack using Dynamic Programming

weights = [1, 3, 4, 6]
values = [2, 6, 7, 10]
capacity = 9


# TOP-DOWN APPROACH

def solve_knapsack(index, limit, dp):

    if index == 0 or limit == 0:
        return 0

    if dp[index][limit] != -1:
        return dp[index][limit]

    # Exclude the current item
    exclude = solve_knapsack(index - 1, limit, dp)

    include = 0

    # Include the item if its weight is within the limit
    if weights[index - 1] <= limit:
        include = values[index - 1] + solve_knapsack(
            index - 1,
            limit - weights[index - 1],
            dp
        )

    dp[index][limit] = max(include, exclude)

    return dp[index][limit]


total_items = len(weights)

dp = [
    [-1] * (capacity + 1)
    for _ in range(total_items + 1)
]

top_result = solve_knapsack(total_items, capacity, dp)

print("Maximum Value using Top-Down:", top_result)


# BOTTOM-UP APPROACH

def knapsack_table(weight_list, value_list, max_capacity):

    count = len(weight_list)

    dp = [
        [0] * (max_capacity + 1)
        for _ in range(count + 1)
    ]

    for item in range(1, count + 1):

        for bag in range(max_capacity + 1):

            # Option 1: Do not choose the item
            dp[item][bag] = dp[item - 1][bag]

            # Option 2: Choose the item
            if weight_list[item -
#coments
# Output:
# Maximum Value using Top-Down: 17
# Maximum Value using Bottom-Up: 17