"""
Recebendo dados do usuário
"""

nome = input("Digite seu nome: ")
print('Seja bem vindo(a) %s' % nome)
print('Seja bem vindo(a) {0}'.format(nome))
print(f'Seja bem vindo(a) {nome}')
idade = input("Qual a sua idade: ")
print('%s tem %s anos.' % (nome,idade))
print('{0} tem {1} anos.'.format(nome,idade))
print(f'{nome} tem {idade} anos.')
