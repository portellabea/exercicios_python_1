#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("********************************************************************************")
print("***************************** LOJA DE TINTAS ***********************************")
print("******************************************************************************** \n")

tamanho_da_pintura = float(input("Insira os metros quadrados da área que será pintada: "))

quantidade_de_tinta = tamanho_da_pintura/3
quantidade_de_lata = round(1 + quantidade_de_tinta/18)
preco_total = quantidade_de_lata * 80.00

print("De acordo com a sua área ({:.2f} m²), você precisará de {:.0f} latas de tinta, com preço total de R${:.2f}.".format(tamanho_da_pintura, quantidade_de_lata, preco_total))


