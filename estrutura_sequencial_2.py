#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganha_por_hora = int(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalha por mês? "))
salario_bruto = ganha_por_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - descontos

print("O seu salário bruto é: R${:.2f}".format(salario_bruto))
print("O tota dos descontos foram: R${:.2f}".format(descontos))
print("O seu salário líquido é: R${:.2f}".format(salario_liquido))

