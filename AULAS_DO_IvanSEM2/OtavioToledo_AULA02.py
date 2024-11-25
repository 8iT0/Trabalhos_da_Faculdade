#QUARTO DE HOTEL (ATIVIDADE 01)
class QuartoDeHotel:
  def __init__(self, n_quarto, tipoquarto, ocupado):
    self.n_quarto=n_quarto
    self.tipoquarto=tipoquarto
    self.ocupado=False
  def verificar(self):
    if not self.ocupado:
      self.ocupado=True
      print(f'o quarto {self.n_quarto} esta ocupado')
    else:
      print(f'o quarto {self.n_quarto} esta livre')
  def reservar(self):
    if self.ocupado==False:
      self.ocupado=True
      print(f'o quarto {self.n_quarto} agora esta reservado')
    else:
      print(f'o quarto {self.n_quarto} ja esta reservado')
#atividade 02
cidades=['FRUTAL','UBERLANDIA', 'UBERABA']
cidade1=['RIO PRETO', 'SÃO CARLOS', 'BARRETOS', 'RIO CLARO', 'SÃO PAULO']
cidadelas= cidades + cidade1
print(cidadelas)

#atividades 03
carros=['gol', 'fusca', 'onix', 'uno', 'voyage']
carros[2:4
       ]=['toro','citrus']
print(carros)

#atividade 04
list01=[]
list02=[]
for i in range(3):
  usuario=input()
  list01.append(usuario)
for i in range(3):
  usuario=input()
  list02.append(usuario)
print(list01)
print(list02)
print(f'{list01+list02}')