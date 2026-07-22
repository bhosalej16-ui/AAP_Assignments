# Fibonacci Using Tabulation (Bottom-Up Dynamic Programming)

n = int(input("Enter the value of N: "))

if n <= 0:
    print("Enter a valid number.")
else:
    fib = [0] * n

    if n >= 1:
        fib[0] = 0
    if n >= 2:
        fib[1] = 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    print("Fibonacci Sequence:")
    for i in range(n):
        print(fib[i], end=" ")