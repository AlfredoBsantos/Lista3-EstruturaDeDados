class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo = Node(valor)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self):
        if self.topo is None:
            print("Pilha vazia!")
            return None
        valor = self.topo.dado
        self.topo = self.topo.proximo
        return valor

    def peek(self):
        if self.topo is None:
            print("Pilha vazia!")
            return None
        return self.topo.dado

    def is_empty(self):
        return self.topo is None

    def exibir(self):
        atual = self.topo
        while atual:
            print(atual.dado, end=' ')
            atual = atual.proximo
        print()



if __name__ == "__main__":
    p = Pilha()
    p.push(10)
    p.push(20)
    p.push(30)

    print("Topo da pilha:", p.peek())

    print("Pilha:")
    p.exibir()

    p.pop()
    print("Após pop:")
    p.exibir()
