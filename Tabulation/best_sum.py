# Solving the Best sum problem using Tabulation method


def best_sum(target_sum: int, numbers: list[int]) -> list | None:
    """
    To return best possibility of achieving a target sum
    """

    table = [None for _ in range(target_sum + 1)]
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] != None:
            for num in numbers:
                if (i + num) <= target_sum and table[i + num] == None:
                    table[i + num] = [*table[i], num]

    return table[target_sum]


print(best_sum(7, [2, 3]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(300, [7, 14]))


"""
m = target sum
n = length of array

Complexity

Time: O(m^2 * n)
Space: O(m^2)
"""
