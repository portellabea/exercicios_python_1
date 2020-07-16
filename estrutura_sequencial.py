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

raio = int(input("Digite o raio para calculo da área do círculo: "))

def area_circulo():
    area = raio * raio * 3.14
    return area

print("A área do círculo é: {}".format(area_circulo()))

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_do_quadrado = int(input("Coloque o lado do quadrado: "))

def area_quadrado():
    area = (lado_do_quadrado * lado_do_quadrado)
    return area * 2

print("O dobro da área é: {}".format(area_quadrado()))

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.


