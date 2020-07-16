#faça um programa que mostre a mensagem "Alo mundo" na tela

print("Hallo Welt")

#faça um programa que peça um numero e então mostre a mensagem "O numero informado foi [numero]

numero_input = int(input("Coloque um número: "))
print("O numero informado foi {}".format(numero_input))

#Faça um Programa que peça dois números e imprima a soma.

x = int(input("Escolha o primeiro número: "))
y = int(input("Escolha o segundo número: "))

def soma(x,y):
    return x + y

print(soma(x,y))

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

indice = 1
nota_total = []

while (indice <= 4):
    nota_input = int(input("Coloque uma nota: "))
    nota_total.append(nota_input)
    indice = indice + 1

def media_das_notas():
    soma_das_notas = (sum(nota_total))
    return soma_das_notas/4

print(media_das_notas())

#Faça um Programa que converta metros para centímetros.

def metros_para_centimetros():
    numero_em_metros = float(input("Coloque o valor em metros para ser convertido: "))
    return numero_em_metros * 100

print("{} cm".format(metros_para_centimetros()))

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("Digite o raio em cm para calculo da área do círculo: "))

def area_circulo():
    area = raio * raio * 3.14
    return area

print("A área do círculo é: {:.2f} cm²".format(area_circulo()))

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_do_quadrado = int(input("Coloque o lado do quadrado em cm: "))

def area_quadrado():
    area = (lado_do_quadrado * lado_do_quadrado)
    return area * 2

print("O dobro da área é: {} cm²".format(area_quadrado()))

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

ganha_por_hora = float(input("Quanto você ganha por hora? "))
numero_de_horas_trabalhadas = int(input("Quantas horas você trabalha no mês? "))

def salario():
    return ganha_por_hora * numero_de_horas_trabalhadas

print("O seu salário é R$ {:.2f}".format(salario()))

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temperatura_farenheit = float(input("Coloque a temperatura em graus Farenheit: "))
temperatura_celsius = 5 * ((temperatura_farenheit-32)/9)

print("A conversão da temperatura {:.1f}ºF é {:.1f}ºC".format(temperatura_farenheit, temperatura_celsius))

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperatura_celsius = float(input("Coloque a temperatura em Celsius: "))
temperatura_farenheit = ((temperatura_celsius * 9)/5) + 32

print("A conversão da temperatura {:.1f}ºC é {:.1f}ºF".format(temperatura_celsius, temperatura_farenheit))

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

numero_01 = int(input("Escolha o primeiro número: "))
numero_02 = int(input("Escolha o segundo número: "))
numero_03 = float(input("Escolha o terceiro número: "))

print((2*numero_01)*(numero_02/2))
print((3*numero_01)+(numero_03))
print(numero_03 * numero_03 * numero_03)

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura_input = float(input("Coloque sua altura: "))
calculo_peso_ideal = (72.7 * altura_input) - 58

print("Seu peso ideal é {:.2f} kg.".format(calculo_peso_ideal))

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura_input = float(input("Coloque sua altura: "))
calculo_peso_ideal_mulheres = (62.1 * altura_input) - 44.7
calculo_peso_ideal_homens = (72.7 * altura_input) - 58

print("Seu peso ideal, de acordo com a sua altura, se você for homem é {:.2f} kg,"
      "se você for mulher é {:.2f} kg".format(calculo_peso_ideal_homens, calculo_peso_ideal_mulheres))

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
# a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_de_peixe = float(input("Coloque o peso do peixe em kg: "))

if (peso_de_peixe > 50):
    excesso = peso_de_peixe - 50
    multa = excesso * 4.00
    print("O peso do peixe foi {:.2f} kg, o excesso foi de {:.2f} kg e a multa foi de R${:.2f}.".format(peso_de_peixe, excesso, multa))
else:
    print("De acordo com o peso do seu peixe, não terá multa.")



print("Fim!")