def replace_first(items, new_value):

    if not items:
        return ()

    items = list(items)
    items[0] = new_value

    return tuple(items)
    # return (new_tuple,) + items[1:]

print(replace_first((1, 2, 3), 9))
print(replace_first(('a',), 'z'))
print(replace_first((), 5))
