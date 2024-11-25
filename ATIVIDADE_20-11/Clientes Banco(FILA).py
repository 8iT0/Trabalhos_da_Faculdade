class Fila():
  def __init__(self):
    self.qnt=[]

  def entrar(self, pessoa):
    self.qnt.append(pessoa)
    print('pessoa adicionada na Fila de Atendimento!\n')

  def atender(self):
    if self.qnt:
      print(f"{self.qnt.pop(0)} foi para atendimento!\n")
    else:
      print("A fila está vazia!")

  def visualizar(self):
    if self.qnt:
      print(f"\nFila atual:{self.qnt}\n")
    else:
      print("A fila está vazia!")

def menu():
  fila=Fila()
  while True:
    print('  _MENU_')
    print(f' 1. Adicionar a fila\n 2. Atender\n 3. Visualizar\n 4. Encerrar\n(escolha a opção pelo Numero)')
    try:
      q=int(input("usuario: "))
    except ValueError:
      print("\nErro de sistema, tente novamente!\n")
      continue
    if q == 1:
      nome=input("Nome do Cliente: ")
      fila.entrar(nome)
    elif q == 2:
      fila.atender()
    elif q == 3:
      fila.visualizar()
    elif q == 4:
      print("Obrigado por Utilizar o Programa!")
      break
    else:
      print('opção invalida tente novamente!')

menu()