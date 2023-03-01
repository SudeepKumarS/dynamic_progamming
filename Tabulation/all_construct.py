# Solving the all construct problem using Tabulation method


def all_construction_possibilites(
    target: str, word_bank: list[str]
) -> list[list[str]] | list[list]:
    """
    This method is used to return all the possibilities of constructing
    the target word using the words in the word bank

    target: str
    word_bank: list[str]
    """
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if (i + len(word)) <= len(target) and target[
                i : (i + len(word))
            ].startswith(word):
                new_combinations = [[*sub_array, word] for sub_array in table[i]]
                table[i + len(word)].extend(new_combinations)

    return table[len(target)]


print(
    all_construction_possibilites(
        "abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
    )
)
print(
    all_construction_possibilites(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
)
print(all_construction_possibilites("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    all_construction_possibilites(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeeeeeee"],
    )
)
