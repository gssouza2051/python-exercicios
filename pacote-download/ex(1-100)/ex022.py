'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''
nome=str(input('Digite seu nome'))
print('Analisando seu nome..')
print('Seu nome com todas as letras maiúsculas fica {} \n e tudo minúscula fica {}'.format(nome.upper(),nome.lower()))
print('Ao todo seu nome todo tem  {} letras \n e  seu primeiro nome tem {} letras'.format(len(nome)-nome.count(' '),nome.find(' ')))
