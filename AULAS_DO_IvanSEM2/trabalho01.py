class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f'Disciplina {disciplina} adicionada ao aluno {self.nome}.')

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            print(f'Disciplina {disciplina} removida do aluno {self.nome}.')
        else:
            print(f'Disciplina {disciplina} não encontrada para o aluno {self.nome}.')

class No:
    def __init__(self, aluno=None):
        self.aluno = aluno
        self.proximo = None

class ListaEncadeadaDeAlunos:
    def __init__(self):
        self.inicio = None

    def adicionar_aluno(self, aluno):
        novo_no = No(aluno)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        print(f'Aluno {aluno.nome} adicionado.')

    def remover_aluno(self, matricula):
        atual = self.inicio
        anterior = None
        while atual is not None and atual.aluno.matricula != matricula:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            print(f'Aluno com matrícula {matricula} não encontrado.')
            return
        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo
        print(f'Aluno com matrícula {matricula} removido.')

    def buscar_aluno(self, matricula):
        atual = self.inicio
        while atual is not None:
            if atual.aluno.matricula == matricula:
                return atual.aluno
            atual = atual.proximo
        print(f'Aluno com matrícula {matricula} não encontrado.')
        return None

    def listar_alunos(self):
        atual = self.inicio
        if atual is None:
            print("Nenhum aluno cadastrado.")
        while atual is not None:
            aluno = atual.aluno
            print(f'Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Disciplinas: {", ".join(aluno.disciplinas)}')
            atual = atual.proximo

def menu():
    lista_alunos = ListaEncadeadaDeAlunos()

    while True:
        print("\nMenu:")
        print("1. Cadastrar um novo aluno")
        print("2. Adicionar uma disciplina a um aluno")
        print("3. Remover uma disciplina de um aluno")
        print("4. Alterar dados do aluno (nome ou matrícula)")
        print("5. Remover aluno")
        print("6. Listar todos os alunos")
        print("7. Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula do aluno: ")
            novo_aluno = Aluno(nome, matricula)
            lista_alunos.adicionar_aluno(novo_aluno)

        elif opcao == '2':
            matricula = input("Matrícula do aluno: ")
            aluno = lista_alunos.buscar_aluno(matricula)
            if aluno:
                disciplina = input("Nome da disciplina: ")
                aluno.adicionar_disciplina(disciplina)

        elif opcao == '3':
            matricula = input("Matrícula do aluno: ")
            aluno = lista_alunos.buscar_aluno(matricula)
            if aluno:
                disciplina = input("Nome da disciplina: ")
                aluno.remover_disciplina(disciplina)

        elif opcao == '4':
            matricula = input("Matrícula do aluno a ser alterado: ")
            aluno = lista_alunos.buscar_aluno(matricula)
            if aluno:
                novo_nome = input("Novo nome do aluno: ")
                nova_matricula = input("Nova matrícula do aluno: ")
                aluno.nome = novo_nome
                aluno.matricula = nova_matricula
                print(f'Dados do aluno {novo_nome} alterados.')

        elif opcao == '5':
            matricula = input("Matrícula do aluno a ser removido: ")
            lista_alunos.remover_aluno(matricula)

        elif opcao == '6':
            lista_alunos.listar_alunos()

        elif opcao == '7':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
