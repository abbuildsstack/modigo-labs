def top_words(text, n):
    # TODO: count word frequency (case-insensitive), then return the top `n`
    # as (word, count) tuples sorted by count descending, ties broken alphabetically
    
    words = text.lower().split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return result[:n]

print(top_words('the cat sat on the mat the cat ran', 2))
print(top_words('a b c', 5))
print(top_words('Go go Go', 1))
print(top_words('', 3))
