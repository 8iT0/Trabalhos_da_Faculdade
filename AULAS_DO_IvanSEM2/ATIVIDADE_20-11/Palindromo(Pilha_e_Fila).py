class Pilha:
    def __init__(self):
        self.itens = []
    def push(self, item):
        self.itens.append(item)
    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    def esta_vazia(self):
        return len(self.itens) == 0


class Fila:
    def __init__(self):
        self.itens = []
    def enqueue(self, item):
        self.itens.append(item)
    def dequeue(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None
    def esta_vazia(self):
        return len(self.itens) == 0


def verificar_palindromo(palavra):
    pilha = Pilha()
    fila = Fila()
    for char in palavra:
        pilha.push(char)
        fila.enqueue(char)
    while not pilha.esta_vazia() and not fila.esta_vazia():
        if pilha.pop() != fila.dequeue():
            return False
    return True


while True:
  print('\n  __verificação de Palindromo:__ \n  (0 para sair)')
  palavra = input("Digite uma palavra: ").lower().replace(" ", "")
  if palavra != "0":
    if verificar_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo.")
  else:
      break
  