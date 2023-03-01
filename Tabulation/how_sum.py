# Solving the how sum problem using Tabulation Method


def how_sum(target_sum: int, numbers: list[int]) -> list | None:
    """
    Method to return an array of elements that can be used to achieve the
    target sum
    """
    table = [None for _ in range(target_sum + 1)]
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] != None:
            for num in numbers:
                if (i + num) <= target_sum:
                    table[i + num] = table[i]
                    table[i + num] = [*table[i + num], num]

    return table[target_sum]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))


"""
m = size of the array
n = length of the array

Complexity

Time: O(m^2 * n)
Space: O(m * m) -> O(m^2)
"""
