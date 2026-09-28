def filter_and_group(catalog, required_tags, excluded_tags):
    # TODO: filter `catalog` by required_tags (must have all) and excluded_tags
    # (must have none), then group matching product names by category
    
    matching_products = {}

    for item in catalog:

        name = item['name']
        product_tags = item['tags']
        category = item['category']
        no_difference = required_tags - product_tags == set()
        no_excluded = excluded_tags & product_tags == set()

        if no_difference and no_excluded:
            matching_products[category] = matching_products.get(category, []) + [name]
                
    return matching_products

catalog = [{'name': 'Laptop', 'category': 'Electronics', 'tags': {'portable', 'new'}}, {'name': 'Desk', 'category': 'Furniture', 'tags': {'wooden'}}]

print(filter_and_group(catalog, {'portable'}, set()))
print(filter_and_group(catalog, set(), {'wooden'}))
print(filter_and_group(catalog, set(), set()))
print(filter_and_group(catalog, {'used'}, set()))
