class Estacao:
    def __init__(self):
        self.fila = []
        self.pilha = []

    def adicionar_vagao(self, vagao):
        self.fila.append(vagao)
        print(f"Vagão {vagao} adicionado à fila.")

    def organizar_vagoes(self):
        while self.fila:
            vagao = self.fila.pop(0)
            while self.pilha and self.pilha[-1] > vagao:
                self.fila.insert(0, self.pilha.pop())
            self.pilha.append(vagao)
        print("Vagões organizados com sucesso.")

    def exibir_estado(self):
        print(f"Fila: {self.fila}")
        print(f"Pilha: {self.pilha}")

    def reiniciar(self):
        self.fila = []
        self.pilha = []
        print("Estação reiniciada.")


def menu():
    estacao = Estacao()
    while True:
        print("\n1. Adicionar Vagão")
        print("2. Organizar Vagões")
        print("3. Exibir Estado")
        print("4. Reiniciar Estação")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                vagao = int(input("Digite o número do vagão: "))
                estacao.adicionar_vagao(vagao)
            case 2:
                estacao.organizar_vagoes()
            case 3:
                estacao.exibir_estado()
            case 4:
                estacao.reiniciar()
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


menu()
