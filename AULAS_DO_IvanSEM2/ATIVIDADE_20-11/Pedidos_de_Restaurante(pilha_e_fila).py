class Restaurante:
    def __init__(self):
        self.fila_pedidos = []
        self.pilha_pratos = []
    def adicionar_pedido(self, pedido):
        self.fila_pedidos.append(pedido)
    def servir_pedido(self):
        if self.fila_pedidos:
            pedido = self.fila_pedidos.pop(0)
            self.pilha_pratos.append(pedido)
    def remover_prato(self):
        if self.pilha_pratos:
            self.pilha_pratos.pop()
    def exibir_estado(self):
        print("Fila de Pedidos:", self.fila_pedidos)
        print("Pilha de Pratos Servidos:", self.pilha_pratos)
restaurante = Restaurante()

while True:
    print("\n1. Adicionar Pedido\n2. Servir Pedido\n3. Remover Prato\n4. Exibir Estado\n5. Sair")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            pedido = input("Digite o pedido: ")
            restaurante.adicionar_pedido(pedido)
        case 2:
            restaurante.servir_pedido()
        case 3:
            restaurante.remover_prato()
        case 4:
            restaurante.exibir_estado()
        case 5:
            break
        case _:
            print("Opção inválida.")
