# Checking the possibility of producing a target sum value using a list of array elements
# Elements in the array can be used multiple times to produce the targe sum


def can_sum(target_sum: int, numbers: list[int]) -> bool:
    """
    This method is used to return a boolean value based on the possibility
    to check whether the target sum can be produced using the list elements
    or not
    """
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers) == True:
            return True
    return False


# print(can_sum(300, [7, 14]))


# Using Memoization
def can_sum_memo(target_sum: int, numbers: list[int], memo: dict = {}) -> bool:
    """
    This method is used to return a boolean value based on the possibility
    to check whether the target sum can be produced using the list elements
    or not
    """
    # Checking in the memo first
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        # Passing the memo object for recursive search
        if can_sum_memo(remainder, numbers, memo) == True:
            # Adding values to memo object
            memo[target_sum] = True
            return True
    # Adding values to memo object
    memo[target_sum] = False
    return False


print(can_sum_memo(300, [7, 14]))
