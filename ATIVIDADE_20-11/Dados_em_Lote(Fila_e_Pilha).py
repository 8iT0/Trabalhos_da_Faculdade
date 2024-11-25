class SensorDataProcessor:
    def __init__(self):
        self.queue = []
        self.stack = []  

    def is_valid_data(self, data):
        return 10 <= data <= 100

    def add_to_queue(self, data):
        self.queue.append(data)
        print(f"Dado {data} adicionado à fila com sucesso!")

    def process_queue(self):
        if not self.queue:
            print("A fila está vazia! Nada para processar.")
            return

        while len(self.queue) > 0:
            data = self.queue.pop(0)
            if self.is_valid_data(data):
                self.stack.append(data)
        print("Fila processada. Dados válidos foram movidos para a pilha.")

    def view_stack(self):
        if not self.stack:
            print("A pilha está vazia! Nenhum dado válido processado.")
        else:
            print("Dados válidos na pilha (ordem inversa):", self.stack[::-1])

    def clear_all(self):
        self.queue.clear()
        self.stack.clear()
        print("Fila e pilha limpas!")


def menu():
    processor = SensorDataProcessor()

    while True:
        print("\n  _MENU_")
        print(" 1. Adicionar dado à fila")
        print(" 2. Processar fila")
        print(" 3. Visualizar dados válidos")
        print(" 4. Limpar fila e pilha")
        print(" 5. Encerrar")
        print("(Escolha a opção pelo número)")

        try:
            option = int(input("Usuário: "))
        except ValueError:
            print("\nErro de sistema, tente novamente!\n")
            continue

        if option == 1:
            try:
                data = int(input("Digite o dado do sensor (número inteiro): "))
                processor.add_to_queue(data)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
        elif option == 2:
            processor.process_queue()
        elif option == 3:
            processor.view_stack()
        elif option == 4:
            processor.clear_all()
        elif option == 5:
            print("Obrigado por utilizar o programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
