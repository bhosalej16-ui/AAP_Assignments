	# Number of Ways to Make Change using Dynamic Programming

coins = list(map(int, input("Enter coin denominations (space separated): ").split()))
amount = int(input("Enter target amount: "))

dp = [0] * (amount + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]

print("Total possible combinations:", dp[amount])