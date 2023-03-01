# This problem is to count the number of possible ways to form
# a target word from an array of words in the array provided


# Brute Force
def count_construct(target: str, word_bank: list[str]) -> int:
    """
    This method is used to count the number of possibilites to form
    the target string using the array elements provided
    """
    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            suffix_count = count_construct(suffix, word_bank)
            total_count += suffix_count

    return total_count


# print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(
#     count_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeeeeeee"],
#     )
# )


# Using Memoization
def count_construct_memo(target: str, word_bank: list[str], memo: dict = {}) -> int:
    """
    This method is used to count the number of possibilites to form
    the target string using the array elements provided
    """
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            suffix_count = count_construct_memo(suffix, word_bank, memo)
            total_count += suffix_count

    memo[target] = total_count
    return total_count


print(count_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct_memo("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    count_construct_memo(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeeeee"],
    )
)


"""
m = target string length
n = word_bank.length

Complexity for Brute Force

Time: O(n^m * m)
Space: O(m * m) --> O(m^2)

Complexity for Memoization Code

Time: O(n * m^2)
Space: O(m * m) -> O(m^2)
"""
