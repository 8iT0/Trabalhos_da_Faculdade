class Texto:
    def __init__(self):
        self.realizadas = [] 
        self.desfeitas = []
        self.atual = ""       

    def realizar(self, texto):
        if self.atual:
            self.realizadas.append(self.atual)
        self.atual = texto
        self.desfeitas.clear()  

    def desfazer(self):
        if self.realizadas:
            self.desfeitas.append(self.atual)
            self.atual = self.realizadas.pop()
        else:
            print("Nada para desfazer!")

    def refazer(self):
        if self.desfeitas:
            self.realizadas.append(self.atual)
            self.atual = self.desfeitas.pop()
        else:
            print("Nada para refazer!")

    def mostrar_texto_atual(self):
        print(f"Texto atual: {self.atual}")

def menu():
  editor=Texto()
  while True:
    print(f'\n   _menu_')
    print(f' 1. adicionar texto\n 2. Desfazer\n 3. Refazer\n 4. Exibir Texto\n 5. Sair')
    try:
      user=int(input('usuario: '))
    except ValueError:
       print("\nErro, insira novamente")
    else:
      match user:
        case 1:
          print('\n _Novo Texto_')
          texto=input("Texto: ")
          editor.realizar(texto)
        case 2:
          editor.desfazer()
          editor.mostrar_texto_atual()
        case 3:
          editor.refazer()
          editor.mostrar_texto_atual()
        case 4:
          editor.mostrar_texto_atual()
        case 5:
          break
        case 6:
          print("Opção Invalida!")

menu()