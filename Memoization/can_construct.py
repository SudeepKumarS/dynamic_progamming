# This problem is to check whether we can form a target word
# from an array of words in the array provided


# Brute Force
def can_construct(desired_word: str, word_bank: list[str]) -> bool:
    """
    This method is used to check whether is it possible to
    achieve the desired word using the array of words provided
    """
    if desired_word == "":
        return True

    for word in word_bank:
        if desired_word.startswith(word):
            suffix = desired_word.removeprefix(word)
            if can_construct(suffix, word_bank) == True:
                return True
    return False


# print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(
#     can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeeeeeee"],
#     )
# )


# Using Memoization
def can_construct_memo(
    desired_word: str, word_bank: list[str], memo: dict = {}
) -> bool:
    """
    This method is used to check whether is it possible to
    achieve the desired word using the array of words provided
    """
    if desired_word in memo:
        return memo[desired_word]

    if desired_word == "":
        return True

    for word in word_bank:
        if desired_word.startswith(word):
            suffix = desired_word.removeprefix(word)
            if can_construct_memo(suffix, word_bank, memo) == True:
                memo[desired_word] = True
                return True
    memo[desired_word] = False
    return False


print(can_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(
    can_construct_memo(
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
