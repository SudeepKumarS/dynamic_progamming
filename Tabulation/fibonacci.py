# Finding a fibonacci of a number using Tabulation Strategy
# Bottom - Up approach


def fibonacci(n: int) -> int:
    """
    To find a fibonacci of a given number
    """
    table = [0] * (n + 1)
    table[1] = 1  # Base scenario of Fibonacci series
    for i in range(
        2, n + 1
    ):  # Starting from 2 as the starting conditions are base scenarios
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))
print(fibonacci(300))


"""
n: size of the input

Complexity using Bottom Up approach
Time: O(n)
Space: O(n)
"""
