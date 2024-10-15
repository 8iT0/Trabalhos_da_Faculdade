def soma(n1,n2):
    ju=n1+n2
    return ju

a=int(input("digite o primeiro valor: "))
b=int(input("Digite o segundo: "))

res= soma(a, b)
print(f"resposta: {res}")

#ATIVADADE 02
def maior_elemento(lista):
    return max(lista)
elementos=[]
while True:
    try:
        per=int(input("insira um numero (0 para encerrar): "))
        if per !=0:
            elementos.append(per)
            res=maior_elemento(elementos)
            print(f"A atual lista é:\n{elementos}\n")
        else:
            break
    except:
        print(f"Erro do codigo escreva novamente\n")
print(f"O maior elemento da lista é: {res}")

#ATIVIDADE 03
def cont_vogais(string):
    vogais = "aeiou"
    contador = {vogal: 0 for vogal in vogais}
    for char in string:
        if char in contador:
            contador[char] += 1
    return contador
while True:
    test=input("Digite uma palavra para fazer contagem(Digite 'fim' para encerrar):\n").replace(" ", "").lower()
    if test == "fim":
        break
    else:
        resultado = cont_vogais(test)
        print(f"Quantidade de vogais na string: {resultado}")

#ATIVIDADE 04
numeros = []
def medias(num):
    numeros.append(num)
    media = sum(numeros) / len(numeros)
    return media
while True:
    entrada = input('Insira os números ("fim" para encerrar): ')
    if entrada.lower() == "fim":
       break
    try:
        numero = float(entrada)
    except ValueError:
        print("Erro! Escreva novamente.")
    else:
        print(f"A média é: {medias(numero)}")

 #ATIVIDADE 05
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numero = int(input("Digite um número: "))
if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

#ATIVIDADE 06
def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = input("Digite uma string: ")
if eh_palindromo(string):
    print(f'"{string}" é um palíndromo.')
else:
    print(f'"{string}" não é um palíndromo.')

#ATIVIDADE 07
def filtro(numeros):
    pares=[num for num in numeros if num % 2 == 0]
    return pares
principal=[]
while True:
    so=input('insira os numeros para criar a lista(digite "fim" para encerrar):')
    if so.lower()=="fim":
        print(f'\nPrograma de criar lista encerrado!\n')
        break
    else:
        num=int(so)
        principal.append(num)
lista_par=filtro(principal)
print(f'A lista criada é:\n {principal}\n\n A lista com numeros pares filtrado é:\n {lista_par}')

#ATIVIDADE 08
def filtrar_strings(lista):
    nova_lista = [string for string in lista if len(string) > 5]
    return nova_lista
lista_de_strings = []
while True:
    nv=input('insira as palavras para a lista ("fim" para encerrar)')
    if nv.lower() == "fim":
        print("lista encerrada")
        break
    else:
        print("palavra adcionada a lista!")
        lista_de_strings.append(nv)
resultado = filtrar_strings(lista_de_strings)
print(resultado) 

#ATIVIDADE 09
def tabuada(num):
    for i in range(1,11):
        print(f'{num}x{i}={num*i}')
        
nu=int(input('insira o numero: '))
print(tabuada(nu))

#ATIVIDADE 10
lista_numero=[]
def cal():
    apresenta=sum(lista_numero)
    print(f"\nLista:\n {lista_numero} \nContem um total de {apresenta}\n")

while True:
    entra=input('insira um numero para entrar na lista (digite "fim" para encerrar):')
    if entra.lower()=="fim":
        print("\ninserção de numeros na lista encerrada!")
        br
    else:
        try:
            numerico=int(entra)
        except:
            print("Erro no preenchimento!")
        else:
            lista_numero.append(numerico)
cal()