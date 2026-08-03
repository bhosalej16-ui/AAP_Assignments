# Dynamic Programming - Fibonacci
# Using Memoization and Tabulation

# Memoization
def fibonacci_memo(n, memo=None):

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation
def fibonacci_tab(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]

    return dp[n]


# Main Program
position = int(input("Enter the Fibonacci Term: "))

ans1 = fibonacci_memo(position)
ans2 = fibonacci_tab(position)

print("\nFibonacci using Memoization :", ans1)
print("Fibonacci using Tabulation  :", ans2)
#coments
Enter the Fibonacci Term: 12

Fibonacci using Memoization : 144
Fibonacci using Tabulation  : 144