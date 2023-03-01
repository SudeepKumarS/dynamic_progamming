# How sum problem takes a target sum input and
# an array of elements to get any one of the possible combinations
# to get the required target sum
# Ex - can_sum(8, [2, 3, 5]) --> [3, 5] or [2, 2, 2, 2]
# In the above example the output can be any of the following two arrays


def how_sum_possibilities(target_sum: int, numbers: list[int]) -> list | None:
    """
    This method is used to return any one of the possibilities
    to acheive the target sum using the given array elements
    """
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        rem = target_sum - num
        rem_result = how_sum_possibilities(rem, numbers)
        if rem_result != None:
            return [*rem_result, num]
    return None


# print(how_sum_possibilities(7, [2, 3]))
# print(how_sum_possibilities(7, [5, 3, 4, 7]))
# print(how_sum_possibilities(300, [7, 14]))


# Using Memoization
def how_sum_possibilities_memo(
    target_sum: int, numbers: list[int], memo: dict = {}
) -> list | None:
    """
    This method is used to return any one of the possibilities
    to acheive the target sum using the given array elements
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        rem = target_sum - num
        rem_result = how_sum_possibilities_memo(rem, numbers, memo)
        if rem_result != None:
            memo[target_sum] = [*rem_result, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(how_sum_possibilities_memo(7, [2, 3], {}))
print(how_sum_possibilities_memo(7, [5, 3, 4, 7], {}))
print(how_sum_possibilities_memo(300, [7, 14], {}))
