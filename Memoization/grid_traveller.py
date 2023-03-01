# Grid Traveller problem
# Finding number of possible ways to reach the end of the grid
def grid_traveller(m: int, n: int) -> int:
    """
    This method is used to return all the unique possible ways
    to travel from the start point to the end point in a grid
    taking only either a right move or down move
    """
    # Base conditions
    if (m == 1) and (n == 1):
        return 1
    if (m == 0) or (n == 0):
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


# print(grid_traveller(1, 1))
# print(grid_traveller(2, 3))
# print(grid_traveller(3, 2))
# print(grid_traveller(3, 3))
# print(grid_traveller(18, 18))


# Using Memoization
def memo_grid_traveller(m: int, n: int, memo: dict = {}) -> int:
    """
    This method is used to return all the unique possible ways
    to travel from the start point to the end point in a grid
    taking only either a right move or down move
    """
    # Generating key to check in the memo
    key = (m, n)
    # Checking whether the grid exists in the memo
    if key in memo:
        return memo[key]
    # Base conditions
    if (m == 1) and (n == 1):
        return 1
    if (m == 0) or (n == 0):
        return 0
    memo[key] = memo_grid_traveller(m - 1, n, memo) + memo_grid_traveller(
        m, n - 1, memo
    )
    return memo[key]


print(memo_grid_traveller(1, 1))
print(memo_grid_traveller(2, 3))
print(memo_grid_traveller(3, 2))
print(memo_grid_traveller(3, 3))
print(memo_grid_traveller(18, 18))
