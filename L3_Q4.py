class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaSimples:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=' ')
            atual = atual.proximo
        print()

    def inverter(self):
        anterior = None
        atual = self.inicio
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.inicio = anterior



if __name__ == "__main__":
    lista = ListaSimples()
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)

    print("Original:")
    lista.exibir()

    lista.inverter()

    print("Invertida:")
    lista.exibir()
