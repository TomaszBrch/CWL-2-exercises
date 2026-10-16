tup = (1,2,3,4)

print(type(tup), len(tup))

try:
     tup[0] = 9
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

def stats(numbers):
    return(min(numbers), max(numbers))

(_max, _min) = stats(tup)

print(f"Max: {_max}")
print(f"Min: {_min}")


