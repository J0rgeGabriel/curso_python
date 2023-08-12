x = 1          #escopo global (acessivel por todo o codigo)

def escopo():
    x = 10     #escopo local (é acessado apenas por nomes do mesmo local)
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)        #escopo global
escopo()        #função foi executada
print(x)        #escopo global