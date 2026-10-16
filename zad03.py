m: list[list[int]] =    [[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12]]
def print_matrix(m:list[list[int]]) -> None:
    for row in m:
        print(" ")
        for num in row:
            print(num, end=" ")

def row_sums(m:list[list[int]]) -> list[int]:
    
    sums: list[int] = []
    for row in m:
        sums.append(sum(row))
    return(sums)
def column_sums(m:list[list[int]]) -> list[int]:


    cols:int = len(m[0])

    rows:int = len(m)

    sums:list[int] = []

    for _ in range(len(m[0])):
        sums.append(0)

    for i in range(cols):
        for j in range(rows):
            sums[i] += m[j][i]

    return(sums)


print(column_sums(m))


def maxiumum(m:list[list[int]]) -> int:
    _max = float('-inf')

    for row in m:
        for num in row:
            if num > _max:  # noqa: PLR1730
                _max = num
    return int(_max)

def transpose(m:list[list[int]]) -> list[list[int]]:

    t_m:list[list[int]] = []

    cols:int = len(m[0])

    rows:int = len(m)

    for _ in range(cols):
        t_m.append([])
    for i in range(cols):
        for j in range(rows):
            t_m[i].append(m[j][i])

    return(t_m)

print(f"Row sums: {row_sums(m)}")
print(f"Column sums: {column_sums(m)}")
print(f"Max: {maxiumum(m)}")
print_matrix(transpose(m))
