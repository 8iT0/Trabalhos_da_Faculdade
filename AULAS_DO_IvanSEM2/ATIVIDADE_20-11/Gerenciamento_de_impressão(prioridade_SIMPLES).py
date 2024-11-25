class FILA:
  def __init__(fila):
    fila.item=[]
  
  def add_tarefa(fila,tarefa,prior):
    fila.item.append((tarefa, prior))
    fila.item.sort(key=lambda x: x[1], reverse=True) 

  def remover_e_imprimir(fila):
    if fila.item:
      tarefa, prior = fila.item.pop(0)
      print(f"{tarefa}(prioridade:{prior}) foi exacutado")
    else:
      print("fila vazia!")
  
  def exibir(fila):
    if fila.item:
      print(fila.item)
    else:
      print('fila vazia!')

def menu():
  Fila=FILA()
  while True:
    print(f'\n   _menu_')
    print(f' 1. adicionar tarefa\n 2. Exibir FILA\n 3. Executar uma tarefa\n 4.Sair')
    user=int(input('usuario: '))
    match user:
      case 1:
        print('\n _adicione um DOC_')
        tarefa=input("Nome: ")
        prior=int(input("Prioridade: "))
        Fila.add_tarefa(tarefa, prior)
      
      case 2:
        Fila.exibir()

      case 3:
        Fila.remover_e_imprimir()

      case 4:
        break

      case _:
        print("Opção Invalida!")

menu()