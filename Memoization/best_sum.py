# Best sum problem takes a target sum input and
# an array of elements to get any one of the possible combinations
# to get the required target sum
# Ex - can_sum(8, [2, 3, 5]) --> [3, 5] or [2, 2, 2, 2] or [2, 3, 3]
# The output for the above example should be [3, 5] as this is the shortest
# possibility of achieving the target sum


# Brute Force
def best_sum_possibility(
    target_sum: int,
    numbers: list[int],
) -> list | None:
    """
    Method used to return the best possibility of combination
    to achieve the target sum
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        rem = target_sum - num
        rem_combination = best_sum_possibility(rem, numbers)
        if rem_combination != None:
            combination = [*rem_combination, num]
            # Checking the shortest combination and update it
            if (shortest_combination == None) or (
                len(combination) < len(shortest_combination)
            ):
                shortest_combination = combination

    return shortest_combination


# print(best_sum_possibility(7, [5, 3, 4, 7]))
# print(best_sum_possibility(8, [2, 3, 5]))
# print(best_sum_possibility(8, [1, 4, 5]))
# print(best_sum_possibility(100, [1, 2, 5, 25]))


# Using Memoization
def best_sum_possibility_memo(
    target_sum: int, numbers: list[int], memo: dict = {}
) -> list | None:
    """
    Method used to return the best possibility of combination
    to achieve the target sum
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        rem = target_sum - num
        rem_combination = best_sum_possibility_memo(rem, numbers, memo)
        if rem_combination != None:
            combination = [*rem_combination, num]
            # Checking the shortest combination and update it
            if (shortest_combination == None) or (
                len(combination) < len(shortest_combination)
            ):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return memo[target_sum]


print(best_sum_possibility_memo(7, [5, 3, 4, 7], {}))
print(best_sum_possibility_memo(8, [2, 3, 5], {}))
print(best_sum_possibility_memo(8, [1, 4, 5], {}))
print(best_sum_possibility_memo(100, [1, 2, 5, 25], {}))


"""
m = target_sum
n = length of numbers

Complexity for Brute Force Code
Time: O(n^m * m)
Space: O(m * m) -> O(m^2)


Complexity for Memoized Code
Time: O(n * m * m) -> O(n * m^2)
Space: O(m * m) -> O(m^2)
"""
