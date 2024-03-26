nome = input("digite Seu nome: ")
altura = float(input('digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2

print(nome)
print(altura)
print(peso)


linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)