def items_to_restock(current_stock, minimum_levels):
    # TODO: loop through current_stock, compare against minimum_levels,
    # and return a list of item names below their minimum
    
    below_minimum = []

    for item, quantity in current_stock.items():
        if item not in minimum_levels:
            continue
        elif quantity < minimum_levels[item]:
            below_minimum.append(item)

    return below_minimum

print(items_to_restock({'rice': 5, 'beans': 20}, {'rice': 10, 'beans': 15}))
print(items_to_restock({'rice': 20}, {'rice': 10}))
print(items_to_restock({'rice': 5, 'sugar': 2}, {'rice': 10}))