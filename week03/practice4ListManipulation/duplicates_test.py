from random import randint
lista = []
listb = []
for i in range (10):
    lista.append(randint(1,101))
print (lista)

for i in range (100):
    i= randint(1,101)
    if i not in lista:
        listb.append(i)
print (listb)
