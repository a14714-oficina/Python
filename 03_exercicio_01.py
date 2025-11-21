# Perguntar a Largura de uma parede.
# De forma aleatória, gere um valor entre 2 e 8 para a altura parede.
#Perguntem pela cor da parede.
# Valor metro quadrado:
#   10 euros se a parede for branca e preta
#   15 euros para outras cores



import random
from random import randint

largura = float(input("Largura da parede em metros: "))
altura = random.randint(2, 8)
cor = input("Cor da parede: ").lower()

area = largura * altura

if cor == ("branca") and cor == ("preta"):
    preco_m2 = 10
else:
    preco_m2 = 15

custo_total = area * preco_m2

print(f"Altura gerada: {altura  :.2f}m")
print(f"Custo total: {custo_total:.2f} euros")