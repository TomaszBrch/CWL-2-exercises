tup:tuple[int,...] = (1,2,3,4)

print(type(tup), len(tup))

try:
     tup[0] = 9  # pyright: ignore[reportIndexIssue]
except TypeError:
    print("Error: tuple is immutable")

print(tup)

(a, b, *rest) = tup

print(f"a: {a}")
print(f"b: {b}")
print(f"rest: {rest}")


print(a,b)

a, b = b, a

print(a,b)

def stats(numbers:tuple[int, ...]) -> tuple[int, int]:
    return(min(numbers), max(numbers))

(_max, _min) = stats(numbers=tup)

print(f"Max: {_max}")
print(f"Min: {_min}")


