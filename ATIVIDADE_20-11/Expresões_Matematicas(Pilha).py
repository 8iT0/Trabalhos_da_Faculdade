class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

def verifica_expressao_balanceada(expressao):
    pilha = Pilha()
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expressao:
        if char in "([{":
            pilha.empilhar(char)
        elif char in ")]}":
            topo = pilha.desempilhar()
            if topo != pares[char]:
                return "Não Balanceada"

    return "Balanceada" if pilha.esta_vazia() else "Não Balanceada"

expressao = "[(a + b) * (c - d)]"
resultado = verifica_expressao_balanceada(expressao)
print(f"Expressão: {expressao}")
print(f"Resultado: {resultado}")