class Soldado:
    def __init__(self, id):
        self.id = id
        self.proximo = None

class Josephus:
    def __init__(self, n):
        self.inicio = self.criar_circulo(n)

    def criar_circulo(self, n):
        primeiro = Soldado(1)
        atual = primeiro
        for i in range(2, n + 1):
            novo = Soldado(i)
            atual.proximo = novo
            atual = novo
        atual.proximo = primeiro  # círculo
        return primeiro

    def resolver(self, passo):
        atual = self.inicio
        eliminados = []

        while atual.proximo != atual:
            for _ in range(passo - 2):  # parar um antes do eliminado
                atual = atual.proximo
            eliminado = atual.proximo
            eliminados.append(eliminado.id)
            atual.proximo = eliminado.proximo  # remove
            atual = atual.proximo  # avança pro próximo

        sobrevivente = atual.id
        return eliminados, sobrevivente



if __name__ == "__main__":
    n = 41  # número de soldados
    d = 3   # conta até 3

    jogo = Josephus(n)
    eliminados, sobrevivente = jogo.resolver(d)

    print("Ordem de eliminação:")
    print(eliminados)
    print("Sobrevivente:", sobrevivente)
