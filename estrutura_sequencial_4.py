#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;

print("********************************************************************************")
print("***************************** LOJA DE TINTAS ***********************************")
print("******************************************************************************** \n")

tamanho_da_pintura = float(input("Insira os metros quadrados da área que será pintada: "))

quantidade_de_tinta = tamanho_da_pintura/6
quantidade_de_lata = round(1 + quantidade_de_tinta/18)
preco_total_lata = quantidade_de_lata * 80.00

quantidade_de_galao = round(1 + quantidade_de_tinta/3.6)
preco_total_galao = quantidade_de_galao * 25.00

print("Somente lata. Quantidade de latas: {:.0f}. Preço final: R$ {:.2f}.".format(quantidade_de_lata, preco_total_lata))
print("Somente galão. Quantidade de galões: {:.0f}. Preço final: R$ {:.2f}.".format(quantidade_de_galao, preco_total_galao))



