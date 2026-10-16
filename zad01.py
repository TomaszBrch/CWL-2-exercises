lista = [0,1,2,3,4,5]

print(lista)

lista.append(6)

print(lista)

lista.remove(3)
print(lista)
lista.insert(3, 66)
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.reverse()

print(lista[1:3])

lista[1:3] = [9,7]
print(lista)
