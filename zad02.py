arr: list[int | str | bool | list[int]] = [4, "hello", True, [0,1,2,3],False,True]

for element in arr:
    print(f'{arr.index(element)}:{type(element).__name__} ')

def filter_by_type(items:list[int | str | bool | list[int]], cls:str) -> list[int | str | bool | list[int]]:
    
    filtered_items = []
    for item in items:
        if type(item).__name__ == cls:
            filtered_items.append(item)  # pyright: ignore[reportUnknownMemberType]
    return(filtered_items)  # pyright: ignore[reportUnknownVariableType]

