class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.inicio = 0
        self.fim = -1
        self.contador = 0

    def adicionar_chamada(self, chamada):
        if self.contador == self.tamanho:
            self.inicio = (self.inicio + 1) % self.tamanho
            self.contador -= 1

        self.fim = (self.fim + 1) % self.tamanho
        self.fila[self.fim] = chamada
        self.contador += 1
        print(f"Chamada '{chamada}' adicionada com sucesso.")

    def atender_chamada(self):
        if self.contador == 0:
            print("Fila vazia! Nenhuma chamada para atender.")
            return None

        chamada_atendida = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.tamanho
        self.contador -= 1
        print(f"Chamada '{chamada_atendida}' atendida.")
        return chamada_atendida

    def visualizar_fila(self):
        print("Fila de chamadas:")
        if self.contador == 0:
            print("Fila vazia!")
        else:
            for i in range(self.contador):
                index = (self.inicio + i) % self.tamanho
                print(f"- {self.fila[index]}")

def menu():
  chamada=FilaCircular(3)
  while True:
    print(f'\n   _menu_')
    print(f' 1. adicionar chamada\n 2. Visualizar Fila\n 3. Atender chamada\n 4. Sair')
    try:
      user=int(input('usuario: '))
    except ValueError:
       print("\nErro, insira novamente")
    else:
      match user:
        case 1:
          print('\n _Adicionar Chamada_')
          Ch=input("Chamada: ")
          chamada.adicionar_chamada(Ch)
        case 2:
          chamada.visualizar_fila()
        case 3:
          chamada.atender_chamada()
        case 4:
          break
        case _:
          print("Opção Invalida!")

menu()