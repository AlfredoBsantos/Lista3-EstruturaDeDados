class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, valor):
        novo = Node(valor)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def desenfileirar(self):
        if self.inicio is None:
            print("Fila vazia!")
            return None
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def frente(self):
        if self.inicio is None:
            print("Fila vazia!")
            return None
        return self.inicio.dado

    def esta_vazia(self):
        return self.inicio is None

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=' ')
            atual = atual.proximo
        print()




if __name__ == "__main__":
    f = Fila()
    f.enfileirar(10)
    f.enfileirar(20)
    f.enfileirar(30)

    print("Frente da fila:", f.frente())

    print("Fila:")
    f.exibir()

    f.desenfileirar()
    print("Após desenfileirar:")
    f.exibir()
