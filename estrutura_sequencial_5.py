#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print("********************************************************************************")
print("*************************** TEMPO DE DOWNLOAD **********************************")
print("******************************************************************************** \n")

tamanho_do_arquivo = float(input("Insira o tamanho do arquivo: "))
velocidade_da_internet = float(input("Insira a velocidade da sua internet: "))
tempo_de_download = round((tamanho_do_arquivo/velocidade_da_internet)/60)

print("O tempo será de aproximadamente {:.0f} minutos".format(tempo_de_download))

