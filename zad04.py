items: list[int] = [1,2,3,4,5,6,7,8,9]
def square_items(items:list[int]) -> list[int]:
    squared_items: list[int] = []

    for item in items:
        squared_items.append(item**2)
    return(squared_items)
def even_items(items:list[int])->list[int]:
    even_items:list[int] = []

    for item in items:
        if item //2 == item /2:
            even_items.append(item)
    return(even_items)
def div_by_3_and_greater_than_5(items:list[int])->list[int]:
    return_items:list[int] = []

    for item in items:
        if item //3 == item /3 and item > 5:
            return_items.append(item)
    return(return_items)
def enumerated_tuples(items:list[int]) -> list[tuple[int, int]]:

    return(list(enumerate(items)))

print(f'Squared items: {square_items(items)}')
print(f'Even items: {even_items(items)}')
print(f'Elements divisable by 3 and greater than 5:{div_by_3_and_greater_than_5(items)}')
print(f'Enumerated tuples: {enumerated_tuples(items)}')