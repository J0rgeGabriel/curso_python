'''Crie uma função que multiplique todos os argumentos não nomeados recebidos.
Retorne o total para uma variavel e mostre o valor da variavel:'''


def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total


print(multiplicacao(1, 2, 3, 4, 5))


'''Crie uma função que fale se o numero é par ou impar:'''


def par_impar(x):
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é impar")
    return x


par_impar(1)
par_impar(2)
par_impar(50*10)
