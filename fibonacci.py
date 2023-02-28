# Correctness of code is good but not efficient
def fibonacci(n: int) -> int:
    """
    This is a method to return the fibonacci series of a number
    """
    if n <= 2:  # Base condition
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))
# print(fibonacci(7))
# print(fibonacci(50))


# Using Memoization
def memo_fibonacci(n: int, memo: dict = {}) -> int:
    """
    This is a method to return the fibonacci series of a number using Memoization
    """
    if (
        n in memo
    ):  # Checking whether already exists in the memo and if not calculate the fibonacci value
        return memo[n]
    if n <= 2:  # Base condition
        return 1
    # Storing the value in memo to use it for the future calculations
    # Passing memo value into the function to use the values
    memo[n] = memo_fibonacci(n - 1, memo) + memo_fibonacci(n - 2, memo)
    return memo[n]


print(memo_fibonacci(6))
print(memo_fibonacci(7))
print(memo_fibonacci(8))
print(memo_fibonacci(50))
