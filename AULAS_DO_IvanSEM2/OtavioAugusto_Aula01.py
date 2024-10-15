#exercicios 1
class pessoa:
  def __init__(self,nome,dt_nasc,rg,sexo):
    self.nome=nome
    self.dt_nasc=dt_nasc
    self.rg=rg
    self.sexo=sexo
  def detalhes(self):
    print(f"nome:{self.nome}\ndata de nascimento:{self.dt_nasc}\nRG:{self.rg}\nsexo:{self.sexo}")
  def comprimentar(self):
    print(f'Voce comprimentou {self.nome}')
  def despedir(self):
    print(f'Voce se despediu de {self.nome}')

nome = input("Digite o nome: ")
dt_nasc = input("Digite a data de nascimento (DD/MM/AAAA): ")
rg = input("Digite o RG: ")
sexo = input("Digite o sexo: ")
eu = pessoa(nome, dt_nasc, rg, sexo)

eu.detalhes()
eu.comprimentar()
eu.despedir()


#exercicios 2
class moto:
  def __init__(self, cor, modelo, ano, cilindrada):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano 
    self.cilindrada = cilindrada
    self.ligada=False
  def ligar(self):
    if not self.ligada:
      self.ligada=True
      print(f"A moto {self.modelo} foi ligada")
    else:
      print(f"A moto {self.modelo} ja esta ligada")
  def desligar(self):
      if self.ligada:
        self.ligada=False
        print(f'a moto {self.modelo} foi desligada')
      else:
        print(f'a moto {self.modelo} ja esta desligada')
  def mostrar_moto(self):
    print(f"cor:{self.cor} modelo:{self.modelo} ano:{self.ano} cilindrada:{self.cilindrada}")

cor=input('Qual a cor da tua moto: ')
modelo=input('O modelo da tua moto: ')
ano= input('O ano dela: ')
cilindrada=input('A cilindrada dela: ')

p1 = moto(cor, modelo, ano, cilindrada)
p1.mostrar_moto()
p1.ligar()
p1.desligar()

#cachorro (atividade 01)
import time
class cachorro:
  def __init__(dog, nome, idade):
    dog.idade=idade
    dog.nome=nome
  def latir(dog):
    print(f'{dog.nome} esta latindo!')
    for i in range(10):
      print('au', end=' ')
      time.sleep(0.5)
nome=input("insira o nome do cachorro: ")
idade=input('insira a idade do cachorro: ')
ca=cachorro(nome, idade)

ca.latir()


#RETANGULO  (atividade 02)
class retangulo:
  def __init__(self, altura, largura):
    self.largura=largura
    self.altura=altura
  def calculo(self):
    total=self.altura * self.largura
    print(F'O total de {self.altura} de altura e {self.largura} de largura é uma area de {total}')
while True:
  larg=input('Insira o valor de largura: ')
  alt=input('Insira o valor de altura: ')
  try:
    larg_int=int(larg) 
    alt_int=int(alt)
    break
  except ValueError:
    print('Erro de valores, por favor insira apenas numericos')
tudo=retangulo(alt_int, larg_int)
tudo.calculo()

#CONTA DE BANCO (ATIVIDADE 03)
class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular=titular
    saldo_int=int(saldo)
    self.saldo_int=saldo_int
  def check(self):
      print(f'titular: {self.titular}\nSaldo: {self.saldo_int}')
  def depositar(self, valordep):
    self.saldo_int+=valordep
    print(f"valor de {valordep} foi depositado com sucesso!")
  def sacar(self, sac):
    if sac>self.saldo_int:
      print(f'valor de saque ({sac}) é excedente ao valor no saldo da conta ({self.saldo_int}), porfavor tente novamente')
    else:
      print(f"valor de {sac}, foi sacado com sucesso! (saldo atual da conta: {self.saldo_int-sac})")
      self.saldo_int-=sac

persona1=ContaBancaria('Roberto', '1500')
persona1.check()
persona1.depositar(100)
persona1.check()
persona1.sacar(1500)
persona1.check()
persona1.sacar(1500)

#CARRO (ATVIDADE 04)
class carro:
  def __init__(cah, cor, modelo, ano):
    cah.cor = cor
    cah.modelo = modelo
    cah.ano = ano 

  def check(cah):
    print(cah.cor, cah.modelo, cah.ano)


cor=input('Qual a cor da tua moto: ')
modelo=input('O modelo da tua moto: ')
ano= input('O ano dela: ')

p1 = carro(cor, modelo, ano)
p1.check()

#ESTUDANTE (ATIVIDADE 05)
class estudante:
  def __init__(a,nome,id_int):
    a.nome=nome
    a.idade=id_int
  def saudação(a):
    print(f"olá {a.nome}!")
nome=input('Nome do estudante: ')
while True:
  idade=input('Idade do estudante: ')
  try:
    id_int=int(idade)
    break
  except ValueError:
    print("!Erro! insira caracteres numericos!")
p1=estudante(nome, id_int)
p1.saudação()

