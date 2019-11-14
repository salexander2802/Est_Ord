def selection_sort(list):
    for i in range(len(list)):                   # Laço externo
        smaller = i                              # Atribui na variavel o valor do indice a ser verificado
        for j in range(i + 1, len(list)):        # Laço interno que verifica se o valor anterior é menor que o próximo valor
            if list[j] < list[smaller]:          # Verifica se o valor anterior é menor que o próximo valor
                smaller = j                      # Caso sim, variavel recebe o indice que compõe o menor valor
        if list[i] != list[j]:                   # Se valores são iguais não é necessaria a troca
            aux = list[i]                        # Variavel aux recebe o valor que está no indice i
            list[i] = list[smaller]              # O indice i recebe o valor do indice j, que possui o valor menor
            list[smaller] = aux                  # O indice da frente recebe valor do indice anterior,o maior na comparação

a = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print(a)
selection_sort(a)                             # Chama a função para ordenar, como parametro o array list
print(a)                                      # Exibe os valores de forma ordenada