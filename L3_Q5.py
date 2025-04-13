import random

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaSimples:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=' ')
            atual = atual.proximo
        print()

    def embaralhar(self):
        # 1. Copiar os valores para uma lista comum
        valores = []
        atual = self.inicio
        while atual:
            valores.append(atual.dado)
            atual = atual.proximo

        # 2. Embaralhar a lista de valores
        random.shuffle(valores)

        # 3. Recriar a lista encadeada com os novos valores
        self.inicio = None
        for valor in reversed(valores):  # reversed pois estamos inserindo no início
            self.inserir_inicio(valor)




if __name__ == "__main__":
    lista = ListaSimples()
    for i in range(1, 6):
        lista.inserir_inicio(i)

    print("Lista original:")
    lista.exibir()

    lista.embaralhar()

    print("Lista embaralhada:")
    lista.exibir()
