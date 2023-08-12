'''
for c in range (1,10):
    print(c)
print("FIM")
'''
"""
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
"""

'''r = "S"
while r == "S":
    n = int(input("Digite um valor:  "))
    r = str(input("Quer continuar? [S/N]")).upper()
print("FIM")'''


'''n = 1
par = 0
impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n %2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} números pares e {impar} números impares")'''

'''
#Ex01:
#Faça um programa que leia o sexo de uma pessoa mas so aceite M ou F. Caso esteja errado peça para digitar novamente:
sexo = input("Digite o seu sexo [M/F]: ").upper()
while sexo not in ("M/F"):
    sexo = input("Sexo invalido, digite novamente o seu sexo [M/F]: ").upper()
print(f"Sexo registrado: {sexo}")
'''
'''
while True:     #o comando While True: é uma estrutura de repetição que cria um loop infinito.
    print("Loop infinito!")
'''
'''
while True:
    for x in range(1,6):
        print(x)
'''

"""#Ex02:
while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    opcao = input("Selecione umas das opções a seguir para continuar:\n"
                "1 - somar\n"
                "2 - subtrair\n"
                "3 - multiplicar\n"
                "4 - dividir\n"
                "5 - maior\n"
                "6 - menor\n"
                "7 - novos números\n"
                "8 - sair do programa\n"
                "O que deseja fazer? ")

    if opcao == "1":
        resultado = n1 + n2
        print(f"A soma de {n1} + {n2} = {resultado}")

    elif opcao == "2":
        selecionar = input(f"Você deseja fazer {n1} - {n2}? [S/N]").upper()
        while selecionar not in("S/N"):
            selecionar = input(f"Valor invalido!! Você deseja fazer {n1} - {n2}? [S/N]").upper()
        if selecionar == "S":
            resultado = n1 - n2
            print(f"O resultado de {n1} - {n2} = {resultado}")
        elif selecionar == "N":
            selecionar = input(f"Você deseja fazer {n2} - {n1}? [S/N]").upper()
            while selecionar not in("S/N"):
                selecionar = input(f"Valor invalido!! Você deseja fazer {n2} - {n1}? [S/N]").upper()
            resultado = n2 - n1
            print(f"O resultado de {n2} - {n1} = {resultado}")

    elif opcao == "3":
        resultado = n1 * n2
        print(f"A multiplicação de {n1} * {n2} = {resultado}")
        
    elif opcao == "4":
        selecionar = input(f"Você deseja fazer {n1} ÷ {n2}? [S/N]").upper()
        while selecionar not in("S/N"):
            selecionar = input(f"VAlOR INVALIDO!! Você deseja fazer {n1} ÷ {n2}? [S/N]").upper()
        if selecionar == "S":
            resultado = n1 / n2
            print(f"O resultado de {n1} ÷ {n2} = {resultado}")

        elif selecionar == "N":
            selecionar = input(f"Você deseja fazer {n2} ÷ {n1}? [S/N]").upper()
            while selecionar not in("S/N"):
                selecionar = input(f"VAlOR INVALIDO!! Você deseja fazer {n2} ÷ {n1}? [S/N]").upper()
            if selecionar == "S":
                resultado = n2 / n1
                print(f"O resultado de {n2} ÷ {n1} = {resultado}")

    elif opcao == "5":
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        else:
            print(f"{n2} é maior que {n1}")

    elif opcao == "6":
        if n1 < n2:
            print(f"{n1} é menor que {n2}")
        else:
            print(f"{n2} é menor que {n1}")
    
    elif opcao == "7":
        continuex
    elif opcao == "8":
        print("Saindo do programa")
        break
    
print("\n")
print("Fim do programa")
"""