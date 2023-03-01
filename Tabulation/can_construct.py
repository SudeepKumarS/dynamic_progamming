# Solving the can construct problem using Tabulation method


def can_construct(target: str, word_bank: list[str]) -> bool:
    """
    This method is used to check whether we can construct a target word using
    the words in the word bank array
    """
    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for i in range(len(target) + 1):
        if table[i] == True:
            for word in word_bank:
                # If the word matches the position
                if (i + len(word)) <= len(target) and target[
                    i : i + len(word)
                ].startswith(word):
                    table[i + len(word)] = True

    print(table)
    return table[len(target)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct(
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
