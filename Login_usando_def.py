# Input

nome = input('Qual o seu nome ? ')
idade = input('Qual a sua idade ? ')

# Variaveis, Listas, Dic, Tupl ...

x = 0
name = ['Luis']
age = ['17']
name += nome
age += idade

# Funções

def msg (msgl):
    return msgl

msgLG = msg (f'BEM VINDO \nNome: {nome}\nIdade: {idade}')

# IF, ELIF & ELSE

if nome in name and idade in age:
    print(msgLG)
else:
    print('Você não está no sistema ainda !')
