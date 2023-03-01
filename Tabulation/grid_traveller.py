# Solving the grid traveller poblem using Bottom Up approach


def grid_traveller(m: int, n: int) -> int:
    """
    To find all the possible ways to travel through a 2D grid
    using Tabulation Strategy
    """
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if (j + 1) <= n:
                table[i][j + 1] += current
            if (i + 1) <= m:
                table[i + 1][j] += current
    return table[m][n]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))


"""
Complexity

Time: O(m * n)
Space: O(m * n)
"""
