class Node:
    def __init__(self, char):
        self.char = char
        self.proximo = None

class ListaString:
    def __init__(self):
        self.inicio = None

    def inserir_final(self, char):
        novo = Node(char)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def carregar_string(self, texto):
        for char in texto:
            self.inserir_final(char)

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.char, end='')
            atual = atual.proximo
        print()

    def substring(self, A, B):
        nova_lista = ListaString()
        atual = self.inicio
        pos = 0
        while atual and pos <= B:
            if pos >= A:
                nova_lista.inserir_final(atual.char)
            atual = atual.proximo
            pos += 1
        return nova_lista


if __name__ == "__main__":
    texto = "txotxo é brabo"
    lista = ListaString()
    lista.carregar_string(texto)

    print("Texto original:")
    lista.exibir()

    print("Substring (3 a 7):")
    nova = lista.substring(3, 7)
    nova.exibir()