import copy


def is_id_changed(a:list[list[int]], b:list[list[int]]) -> None:
    if a is not b:
        print("id changed")
    else:
        print("id unchanged")

def is_changed(a:list[list[int]], b:list[list[int]]) -> None:
    if a == b:
        print("changed")
    else:
        print("unchanged")
a: list[list[int]] = [[1,2,3,4,5]]


#przypisanie
b: list[list[int]] = a

# print(f"ID a: {id(a)}, ID b: {id(b)}")
is_id_changed(a=a, b=b)

#kopia płytka
b_copy_shallow: list[list[int]] = a.copy()
# print(f"ID a: {id(a)}, ID b_copy_shallow: {id(b_copy_shallow)}")
is_id_changed(a=a, b=b_copy_shallow)
#kopia głęboka
b_copy_deep : list[list[int]] = copy.deepcopy(x=a)
# print(f"ID a: {id(a)}, ID b_copy_deep: {id(b_copy_deep)}")
is_id_changed(a=a,b=b_copy_deep)

#zmiana elementu w kopii

a[0][0] = 7




print(f"This is b after change {b}")
is_changed(a=a,b=b)
print(f"This is b_copy shallow after change {b_copy_shallow}")
is_changed(a=a,b=b_copy_shallow)
print(f"This is b_copy_deep after change {b_copy_deep}")
is_changed(a=a, b=b_copy_deep)