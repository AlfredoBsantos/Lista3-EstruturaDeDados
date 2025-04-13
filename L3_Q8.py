class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None

class ListaPessoas:
    def __init__(self):
        self.inicio = None

    def inserir(self, nome, idade):
        nova = Pessoa(nome, idade)
        nova.proximo = self.inicio
        self.inicio = nova

    def exibir(self):
        atual = self.inicio
        while atual:
            print(f"{atual.nome} - {atual.idade} anos")
            atual = atual.proximo

    def to_lista(self):
        # Converte para lista Python comum
        lista = []
        atual = self.inicio
        while atual:
            lista.append((atual.nome, atual.idade))
            atual = atual.proximo
        return lista

    def ordenar_por_nome(self):
        nova_lista = ListaPessoas()
        pessoas = sorted(self.to_lista(), key=lambda x: x[0].lower())
        for nome, idade in reversed(pessoas):
            nova_lista.inserir(nome, idade)
        return nova_lista

    def ordenar_por_idade(self):
        nova_lista = ListaPessoas()
        pessoas = sorted(self.to_lista(), key=lambda x: x[1])
        for nome, idade in reversed(pessoas):
            nova_lista.inserir(nome, idade)
        return nova_lista




if __name__ == "__main__":
    lista = ListaPessoas()
    lista.inserir("Carlos", 25)
    lista.inserir("Amanda", 20)
    lista.inserir("Bruno", 22)
    lista.inserir("Daniela", 19)

    print("Original:")
    lista.exibir()

    print("\nOrdenado por nome:")
    por_nome = lista.ordenar_por_nome()
    por_nome.exibir()

    print("\nOrdenado por idade:")
    por_idade = lista.ordenar_por_idade()
    por_idade.exibir()
