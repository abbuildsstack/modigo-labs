def fulfill_orders(stock, orders):
    # TODO: process orders in sequence against a working copy of stock.
    # Fulfill only orders where every item is fully available; deduct nothing
    # for rejected orders. Do not modify the `stock` argument.

    fulfilled = []
    rejected = []
    remaining = stock.copy()

    # for order in orders
    for order in orders:
        can_fulfill = True
        order_id = order['id']
        needed = order['items']

        for item, quantity in needed.items():
            if item not in remaining or quantity > remaining[item]:
                can_fulfill = False
                break
        
        if can_fulfill:
            for item, quantity in needed.items():
                remaining[item] -= quantity
            
            fulfilled.append(order_id)
        
        else:
            rejected.append(order_id)
            

    return {'fulfilled': fulfilled, 'rejected': rejected, 'remaining_stock': remaining}

print(fulfill_orders({'apple': 5}, [{'id': 'o1', 'items': {'apple': 2}}, {'id': 'o2', 'items': {'apple': 4}}]))
print(fulfill_orders({'a': 5, 'b': 1}, [{'id': 'o1', 'items': {'a': 2, 'b': 5}}]))