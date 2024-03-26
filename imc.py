
# Funçao para calcular o (IMC)
def calcular_IMC(peso, altura):
    imc = peso / altura ** 2
    return imc

# Solicitaçõe de dados do usuario
nome = input("digite Seu nome: ")

altura = float(input('digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))

# Calculo do (IMC)
imc = calcular_IMC(peso, altura)

classificacao =(f'Seu IMC é de: {imc:.2f}')


# Logica do programa
if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif 18.5 <= imc < 24.9:
    classificacao = 'Peso normal'
elif 24.9 <= imc < 29.9:
    classificacao = 'Sobrepesso'
elif 29.9 <= imc < 34.9:
    classificacao = ('Obesidade grau I.')
elif 34.9 <= imc < 39.9:
    classificacao = ('Obesidade grau II (severa).')
else:
    classificacao = ('Obesidade grau III (mórbida).')

# Resultados
print(f'seu IMC é de : {imc:.2f}')
print(f'Sua classificação é de : {classificacao}')