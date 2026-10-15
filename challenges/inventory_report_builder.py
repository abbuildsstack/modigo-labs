# No starter code provided. Write the full function yourself.
# Function name: inventory_report
# Parameter: items (a list of (name, quantity, price) tuples)
# Must return: a dict with "total_value", "most_valuable", and "low_stock"

def inventory_report(items):

    total_value = 0
    highest = -1
    most_valuable = None
    low_stock = []

    for name, quantity, price in items:
        total_amount = quantity * price
        total_value += total_amount

        if total_amount > highest:
            highest = total_amount
            most_valuable = name

        if quantity < 5:
            low_stock.append(name)

    return {'total_value': round(total_value, 2), 'most_valuable': most_valuable, 'low_stock': sorted(low_stock)}

print(inventory_report([('pen', 10, 1.5), ('book', 2, 12.0), ('bag', 4, 20.0)]))
print(inventory_report([('a', 5, 1)]))
print(inventory_report([]))
