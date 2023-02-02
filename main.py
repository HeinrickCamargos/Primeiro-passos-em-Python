'''
Autor: Heinrick Camargos
Data: 30/01/2023    
Versão: 1.0

'''

# Formulario simples  

nome = input('Qual é o seu nome: ')
idade = input('Qual é o sua idade: ')
idade = str(idade)
cidade = input('Em qual cidade você mora: ')

print ('O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

# Formulario simples formatado

nome = 'Sabrynna'
sobrenome = 'Silva'
profissao = 'Professora'

texto = f'a {nome} {sobrenome} e um execelente [{profissao}]'

print(texto)

# manipulação de dados

x = str(3)
y = int(4)
z = float (5)

print (x = x)
print (y = y)
print (z = z)

#

nome = 'Sabrynna'
idade = 32
idade = str(idade)
cidade = 'brasilia'

print ('A ' + nome + 'tem ' + idade + 'anos de idade e mora em ' + cidade + '.')

# usando ipunt 

nome = input ('Qual é o seu nome: ')
idade = input ('Qual é a sua idade: ')
idade = str(idade)
cidade = input('Onde você mora: ')

print('O ' + nome + ' tem ' + idade + ' anos de idade e mora no ' + cidade + '.')

# calculadora de idade 

ano_nascimento = input('Em que ano você nasceu ?')
idade + 2023 - int(ano_nascimento)

print(idade)

# usando o slice (index)

fruta = 'Abacate'
#index 0123456

print(fruta[2:5])

fruta = 'Abacate'
#index 0123456

print(fruta[-1])

valor = '23.56'
valor = str(valor)
#index 01234

print(valor[2:5])
