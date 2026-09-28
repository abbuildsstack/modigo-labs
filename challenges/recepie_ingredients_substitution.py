def can_make_recipe(pantry, recipe, substitutes):
    # TODO: for each ingredient in `recipe`, check if pantry has enough directly,
    # or if any listed substitute has enough on its own
    
    for ingredient, qty_needed in recipe.items():

        is_satisfied = False

        if ingredient in pantry and qty_needed <= pantry[ingredient]:
            is_satisfied = True
        elif ingredient in substitutes:
            for substitute in substitutes[ingredient]:
                if substitute in pantry and qty_needed <= pantry[substitute]:
                    is_satisfied = True
                    break
        
        if not is_satisfied:
            return False

    return True

print(can_make_recipe({'flour': 2, 'sugar':1}, {'flour': 1, 'sugar': 1}, {}))
print(can_make_recipe({'flour': 2}, {'flour': 1, 'sugar': 1}, {}))
print(can_make_recipe({'flour': 2, 'honey': 3}, {'flour': 1, 'sugar': 1}, {'sugar': {'honey', 'maple syrup'}}))
print(can_make_recipe({'flour': 2, 'honey': 0}, {'flour': 1, 'sugar': 1}, {'sugar': {'honey'}}))
