def find_lcs(text1, text2):
    rows = len(text1)
    cols = len(text2)

    # DP matrix
    table = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    # Build DP table
    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            if text1[x - 1] == text2[y - 1]:
                table[x][y] = table[x - 1][y - 1] + 1
            else:
                table[x][y] = max(table[x - 1][y], table[x][y - 1])

    # Reconstruct LCS
    x = rows
    y = cols
    result = []

    while x > 0 and y > 0:
        if text1[x - 1] == text2[y - 1]:
            result.append(text1[x - 1])
            x -= 1
            y -= 1
        elif table[x - 1][y] >= table[x][y - 1]:
            x -= 1
        else:
            y -= 1

    result = result[::-1]

    return ''.join(result), table[rows][cols]


# Driver Code
a = input("Enter first string: ")
b = input("Enter second string: ")

sequence, count = find_lcs(a, b)

print("\nLCS is:", sequence)
print("LCS Length is:", count)
# Output:
# Enter first string: ABCDGH
# Enter second string: AEDFHR
#
# LCS is: ADH
# LCS Length is: 3
#
# Enter first string: XMJYAUZ
# Enter second string: MZJAWXU
#
# LCS is: MJAU
# LCS Length is: 4
