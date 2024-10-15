caixa=[]
clientes = []
produtos = []

while True:
    print("\nMenu de opções:")
    print("1. Cliente")
    print("2. Produto")
    print("3. Caixa")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        class Cliente:
            def __init__(self, nome, fone):
                self.nome = nome
                self.fone = fone


        def adicionar_cliente():
            nome = input("Digite o nome do cliente: ")
            fone = input("Digite o Numero do cliente: ")
            cliente = Cliente(nome, fone)
            clientes.append(cliente)
            print(f"CLiente {nome} adicionado.")

        def remover_cliente():
            nome = input("Digite o nome do cliente a ser removido: ")
            for cliente in clientes:
                if cliente.nome == nome:
                    clientes.remove(cliente)
                    print(f"Cliente '{nome}' foi removido.")
                    break
            else:
                print(f"O cliente '{nome}' não  foi encontrado.")

        def exibir_cliente():
            print("\nLista de Clientes:")
            for cliente in clientes:
                print(f"Nome: {cliente.nome}, Numero: {cliente.fone}")

        while True:
            print("\nMenu de opções:")
            print("1. Adicionar Cliente")
            print("2. Remover Cliente")
            print("3. Exibir todos os clientes")
            print("4. Sair")
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                adicionar_cliente()
            elif opcao == 2:
                remover_cliente()
            elif opcao == 3:
                exibir_cliente()
            elif opcao == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
        
    elif opcao == 2:
        class Produto:
            def __init__(self, nome, total, val, qnt):
                self.nome = nome
                self.total = total
                self.val = val
                self.qnt = qnt


        def adicionar_produto():
            nome = input("Digite o produto: ")
            val = float(input("Digite o valor: "))
            qnt= float(input("Digite a quatidade: "))
            total = qnt * val
            produto = Produto(nome, total, val, qnt)
            produtos.append(produto)
            print(f"O produto {nome} foi adicionado.")
            
        def exibir_produto():
                print("\nLista de Produtos:")
                for produto in produtos:
                    print(f"Nome: {produto.nome}, Numero: {produto.val}, Quantidade: {produto.qnt}, Total: {produto.total}")

        def calcular_val():
            total_produtos = sum(produto.total for produto in produtos)
            print(f"Total do valor de estoque: R${total_produtos:.2f}")
            
        while True:
            print("\nMenu de opções:")
            print("1. Cadastrar produto")
            print("2. Mostrar Todos Produtos")
            print("3. Somar Valor Total")
            print("4. Sair")
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                adicionar_produto()
                
            elif opcao == 2:
                exibir_produto()
                
            elif opcao == 3:
                calcular_val()
                
            elif opcao == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    elif opcao == 3:
            while True:
                print("1. Adicionar receita")
                print("2. Adicionar despesa")
                print("3. Mostrar movimentação e saldo")
                print("4. Voltar")
                escolha = int(input('escolha uma das opções'))
                if escolha == 1:
                    tipo=input("Qual o tipo: ")
                    descricao=input("Descrição: ")
                    valor=float(input("Valor: "))
                    caixa.append({'tipo': tipo, 'descricao': descricao, 'valor' : valor})
                elif escolha == 2:
                    tipo=input("Qual o tipo: ")
                    telefone=input("Descrição: ")
                    valor=float(input("Valor: "))
                    caixa.append({'tipo': tipo, 'descricao': descricao, 'valor' : valor})
                elif escolha == 3:
                    saldo = sum(item['valor'] if item['tipo'] == 'receita' else -item['valor'] for item in caixa)
                    print("Movimentação do caixa:")
                    for item in caixa:
                        print(f"{item['tipo']}: {item['descricao']} - R$ {item['valor']:.2f}")
                    print(f"Saldo: R$ {saldo:.2f}")
                elif escolha == 4:
                        break

            
                
    elif opcao==4:
        sair = input("tem certeza que deseja sair?  ").lower()
        if sair == "sim":
            break
        
    else:
        print("Opção inválida. Tente novamente.")