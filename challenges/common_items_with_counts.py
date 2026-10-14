def common_with_counts(list1, list2):
    # TODO: return shared items, each repeated only as often as it
    # appears in both lists, in the order of list1
    shared = []
    count = {}

    for num in list2:
        count[num] = count.get(num, 0) + 1
    
    for num in list1:
        if num in count and count[num] > 0:
            shared.append(num)
            count[num] -= 1

    return shared

print(common_with_counts([1, 2, 2, 3], [2, 2, 2, 4]))
print(common_with_counts([1, 1, 2], [1, 2, 2]))
print(common_with_counts([1, 2], [3, 4]))
