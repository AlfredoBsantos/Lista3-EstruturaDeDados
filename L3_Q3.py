class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo  # guarda o índice do próximo nó

class ListaSimplesArray:
    def __init__(self):
        self.nos = []      # lista para armazenar os nós
        self.inicio = None # índice do primeiro nó

    def inserir_inicio(self, valor):
        novo_indice = len(self.nos)
        novo_no = Node(valor, self.inicio)
        self.nos.append(novo_no)
        self.inicio = novo_indice

    def inserir_fim(self, valor):
        novo_indice = len(self.nos)
        novo_no = Node(valor, None)
        self.nos.append(novo_no)

        if self.inicio is None:
            self.inicio = novo_indice
        else:
            atual = self.inicio
            while self.nos[atual].proximo is not None:
                atual = self.nos[atual].proximo
            self.nos[atual].proximo = novo_indice

    def exibir(self):
        atual = self.inicio
        while atual is not None:
            print(self.nos[atual].valor, end=' ')
            atual = self.nos[atual].proximo
        print()



if __name__ == "__main__":
    lista = ListaSimplesArray()
    lista.inserir_fim(10)
    lista.inserir_fim(20)
    lista.inserir_inicio(5)
    lista.inserir_fim(30)

    print("Lista:")
    lista.exibir()
