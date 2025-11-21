from random import randint

num = randint(1,20)

if num > 10:
    print("Valor aleatório maior que 10")
else:
    print("Valor aleatório menor que 10")
#Maior que 12, menor que 8 ou entre 8 e 12
if num > 12:
    print("Maior que 12")
elif num < 8:
    print("Menor que 8")
else:
    print("Entre 8 e 12")
if (num >= 8) and (num <=12):
    print("Dentro")
