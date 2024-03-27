
# Funçao para calcular o (IMC)
def calcular_IMC(peso, altura):
    imc = peso / altura ** 2
    return imc

# Solicitaçõe de dados do usuario
nome = input("digite Seu nome: ")

altura = float(input('digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))

# Função de peso ideal
def calculo_de_peso_ideal(altura):
    # imc ideal é 18.5 á 24.9
    imc_ideal_min = 18.5
    imc_ideal_max = 24.9
    peso_ideal_min = imc_ideal_min * (altura ** 2)
    peso_ideal_max = imc_ideal_max * (altura ** 2)
    return peso_ideal_min, peso_ideal_max

def calcular_quantos_a_perde(peso_atual, peso_ideal_max):
    if peso_atual > peso_ideal_max:
        return peso_atual - peso_ideal_max
    else :
        return
    
# Calculo do (IMC)
imc = calcular_IMC(peso, altura)

peso_ideal_min, peso_ideal_max = calculo_de_peso_ideal(altura)

peso_a_perde = calcular_quantos_a_perde(peso, peso_ideal_max)






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
print(f'Seu peso ideal é entre {peso_ideal_min:.2f} kg e {peso_ideal_max:.2f}kg')
if peso_a_perde > 0:
    print(f'Voce precisa perde pelo menos {peso_a_perde:.2f} kg para alcançar o peso ideal')
else:
    print(f'Voce está dentro do peso ideal')