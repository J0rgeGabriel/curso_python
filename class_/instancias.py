# Hard coded: é algo que foi escrito diretamento no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f"{self.nome} está acelerando...")

string = "Jorge"
print(string.upper())

print()

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

print()

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()