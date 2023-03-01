# Solving the count construct problem using Tabulation method


def count_construct(target: str, word_bank: list[str]) -> int:
    """
    To return the count of possibilities of forming a target word
    using a word bank
    """
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target) + 1):
        if table[i] != 0:
            for word in word_bank:
                if (i + len(word)) <= len(target) and target[
                    i : (i + len(word))
                ].startswith(word):
                    table[i + len(word)] += table[i]

    return table[len(target)]


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeeeee"],
    )
)

"""
m = target word length
n = word bank length

Complexity

Time: O(m^2 * n)
Space: O(m)
"""
