
'''Faça um programa qua leia um número Inteiro e mostre na tela o seu sucessor e seu antecassor.'''
numero = int(input("Digite um numero: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"Aalisando o número {numero}, o seu antecessor é {antecessor} e seu secessor é {sucessor}")

'''Cria um algoritmo qua laia um númaro e mostre  o sau dobro, triplo e raiz quadrada.'''
numero = float(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** 0.5
print(f"De acordo com o número {numero}, o seu dobro é {dobro}, seu triplo é {triplo} e a sua \
raiz quadrada é {round(raizQuadrada, 2)}")

'''Escrava um programa qua leia um valor em matros a o exiba convertido em cantimatros e milimatros'''
metros = float(input("Digite uma distancia em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"A medida de {metros}m corrensponde a {centimetros}cm e a {milimetros}mm")

'''Faça um programa qua leia um número inteiro qualquer e mostre na tala a sua tabuada'''
numero = float(input("Digite um numero que vamos fazer a tabuada dele: ").replace(",","."))
x1 = print(f"{numero} x 1 é igual a {round(numero * 1, 2)}")
x2 = print(f"{numero} x 2 é igual a {round(numero * 2, 2)}")
x3 = print(f"{numero} x 3 é igual a {round(numero * 3, 2)}")
x4 = print(f"{numero} x 4 é igual a {round(numero * 4, 2)}")
x5 = print(f"{numero} x 5 é igual a {round(numero * 5, 2)}")
x6 = print(f"{numero} x 6 é igual a {round(numero * 6, 2)}")
x7 = print(f"{numero} x 7 é igual a {round(numero * 7, 2)}")
x8 = print(f"{numero} x 8 é igual a {round(numero * 8, 2)}")
x9 = print(f"{numero} x 9 é igual a {round(numero * 9, 2)}")
x10 =print(f"{numero} x 10 é igual a {round(numero * 10, 2)}")
