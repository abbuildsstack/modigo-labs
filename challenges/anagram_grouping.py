def group_anagrams(words):
    # TODO: group words that are anagrams of each other, preserving first-seen order
    group = {}

    for word in words:
        anagram = ''.join(sorted(word))

        if anagram not in group:
            group[anagram] = []

        group[anagram].append(word)

    return list(group.values())

print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
