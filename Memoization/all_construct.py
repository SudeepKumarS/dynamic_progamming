# All consturction possibilities to construct a target
# using the word bank


# Brute Force
def all_construction_possibilites(
    target: str, word_bank: list[str]
) -> list[list[str]] | list:
    """
    This method is used to return all the construction possibilities
    using the list of words provided
    """
    if target == "":
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            rem = target.removeprefix(word)
            result_possibilities = all_construction_possibilites(rem, word_bank)
            final_possibilities = list(map(lambda x: [word, *x], result_possibilities))
            result.extend(final_possibilities)
    return result


# print(
#     all_construction_possibilites(
#         "abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
#     )
# )
# print(
#     all_construction_possibilites(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
#     )
# )
# print(all_construction_possibilites("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(
#     all_construction_possibilites(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeeeeeee"],
#     )
# )


# Using Memoization
def all_construction_possibilites_memo(
    target: str, word_bank: list[str], memo: dict = {}
) -> list[list[str]] | list:
    """
    This method is used to return all the construction possibilities
    using the list of words provided
    """
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            rem = target.removeprefix(word)
            result_possibilities = all_construction_possibilites_memo(
                rem, word_bank, memo
            )
            final_possibilities = list(map(lambda x: [word, *x], result_possibilities))
            result.extend(final_possibilities)
    memo[target] = result
    return result


print(
    all_construction_possibilites_memo(
        "abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
    )
)
print(
    all_construction_possibilites_memo(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
)
print(all_construction_possibilites_memo("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    all_construction_possibilites_memo(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeeeee", "f"],
        {},
    )
)


"""
Complexity for worst case even for Memoized code

Time: O(n^m)
Space: O(m)

"""
