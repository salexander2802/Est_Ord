def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        

a = [8,5,12,55,3,7,82,44,44,35,25,41,29,17]
print (a)
bubble_sort(a)
print(a)
