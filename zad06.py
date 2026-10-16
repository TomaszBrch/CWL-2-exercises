items = [[1,2,3,4,5]]

new_items = items

print(f"Items id: {id(items)}")
print(f"New items id: {id(items)}")

new_items_copy = items.copy()

print(f"New items copy id: {id(items)}")
