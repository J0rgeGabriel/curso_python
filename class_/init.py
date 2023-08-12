#string = "Jorge"  #str
#print(string.upper())
#print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Jorge", "Gabriel")
print(f"{p1.nome} {p1.sobrenome}")

p2 = Pessoa("Monica", "de Souza")
print(f"{p2.nome} {p2.sobrenome}")
