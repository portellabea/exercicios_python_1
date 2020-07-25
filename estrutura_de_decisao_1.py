# Faça um Programa que peça dois números e imprima o maior deles.
from typing import List

numbers: List[int] = []
indice = 0

while indice < 2:
    numbers.append(int(input("Choose a number: ")))
    indice += 1

print(numbers)
print(max(numbers))

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = int(input("Choose a number: "))

if value > 0:
    print("The number you selected is positive.")
elif value == 0:
    print("The number you selected is zero.")
else:
    print("The number you selected is negative.")

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


