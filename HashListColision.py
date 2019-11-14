class Lista:

     def __init__(self):
          self.lista=[]

     def vazio(self): #verifica se lista está vazia
          return len(self.lista) == 0 #retorna True ou False

     def insere_lista(self, item): #insere item no final da lista
         self.lista.append(item)

     def pesquisa_lista(self, chave): #procura item na lista
          for i in self.lista:
               if i == chave:
                    return True
          return False

     def apaga_lista(self, chave): #apaga item informado
         self.lista.remove(chave)
     
     def imprime_lista(self):
          for i in self.lista:
               print("%d -> " %i, end="")              

# fim Classe Lista

class HashListaColisao:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return (v%int(self.tam_max))

     def insere(self, item):
          pos = self.funcaohash(item)          
          if self.tab.get(pos) == None: # se posicao vazia 
               self.tab[pos] = Lista()
          else:
               if self.tab[pos].pesquisa_lista(item):
                    print(" *** ATENCAO O item %d ja foi cadastrado ***" %item)
                    return
          self.tab[pos].insere_lista(item)

     def apaga(self, chave):
          pos = self.busca(chave)
          if pos == -1:
               print(" Item nao encontrado")
          else:
               self.tab[pos].apaga_lista(chave)

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] -> " %i, end="")
               self.tab[i].imprime_lista()
               print("null")

     def busca(self, chave):
          pos = self.funcaohash(chave)
          if self.tab[pos].pesquisa_lista(chave):
               return pos
          return -1
     
# fim Classe HashListaColisao

tamanhoHash = 7
tab = HashListaColisao(tamanhoHash)
print("\n****************************************************")
print("      Tabela HASH Colisoes Lista (%d itens) " %tamanhoHash)
print("****************************************************")
for i in range (0,tamanhoHash,1):
     print("\nInserindo item %d" %(i + 1))
     item = int(input(" - Forneca valor: "))
     tab.insere(item)
print("\nImprimindo conteudo")
tab.imprime()
item = int(input("\n - Forneca valor para buscar: "))
pos = tab.busca(item)
if pos == -1:
     print("-> Item nao encontrado")
else:
     print("-> Item encontrado na posicao: ", pos)
item = int(input("\n - Forneca valor para apagar: "))
tab.apaga(item)
print("\nImprimindo conteudo")
tab.imprime()
print("\n")