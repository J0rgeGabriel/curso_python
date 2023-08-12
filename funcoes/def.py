def python():
    print('teste - 1')
    print('teste - 2')
    print('teste - 3')
    print('teste - 4')


python()
print()
python()


def imprimir(a, b, c):
    return max(a, b, c)

print(imprimir(1, 2, 3))
print(imprimir(10, 20, 30))
print(imprimir(100, 200, 300))


def saudacao(nome="Sem nome"):
    print(f'Olá {nome}')


saudacao("Jorge")
saudacao("Gabriel")
saudacao()
saudacao("")


def multiplo_de(numero, multiplico):
    resultado = numero % multiplico == 0
    print(f"{numero} é multiplo de {multiplico}?", end=" ")
    print(resultado)


multiplo_de(10, 2)
multiplo_de(16, 8)
multiplo_de(25, 3)
multiplo_de(103, 2)


def soma(x, y, z):
    print(f"{x=} {y=} {z=}", "|", "x + y + z =", x + y + z)


soma(1, 2, 3)
soma(10, 20, 30)
soma(100, 200, 300)


def soma(x, y, z = None):
    if z is not None:
        print(f"{x=} + {y=} + {z=} = {x + y + z}")
    else:
        print(f"{x=} + {y=} = {x + y}")


soma(1, 2)
soma(10, 20)
soma(100, 200)
soma(1, 2, 3)