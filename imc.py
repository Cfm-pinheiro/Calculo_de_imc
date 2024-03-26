
def calcular_IMC(peso, altura):
    imc = peso / altura ** 2
    return imc

nome = input("digite Seu nome: ")

altura = float(input('digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))

imc = calcular_IMC(peso, altura)

print(f'Seu IMC é de: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif 18.5 <= imc < 24.9:
    print('Você está no peso ideal.')
elif 24.9 <= imc < 29.9:
    print('Você está acima do peso ideal (sobrepeso).')
elif 29.9 <= imc < 34.9:
    print('Obesidade grau I.')
elif 34.9 <= imc < 39.9:
    print('Obesidade grau II (severa).')
else:
    print('Obesidade grau III (mórbida).')

    
    linha_3 = f'{imc:.2f}'
    print(linha_3)

'''
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

'''