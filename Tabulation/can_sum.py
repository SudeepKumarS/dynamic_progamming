# Solving the can sum problem using Tabulation method


def can_sum(target: int, numbers: list[int]) -> bool:
    """
    To check whether we can produce the target sum using the elements
    in the array provided
    """
    table = [False for _ in range(target + 1)]
    table[0] = True
    for i in range(target + 1):
        if table[i] == True:
            for j in numbers:
                if (i + j) <= target:
                    table[i + j] = True

    return table[target]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))


"""
m = Size of the target
n = length of the array


Complexity

Time: O(m * n)
Space: O(m)
"""
