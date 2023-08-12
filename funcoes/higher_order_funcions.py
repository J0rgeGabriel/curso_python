def saudacao(msg, nome):
    return f"{msg}, {nome}!"

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, "Boa tarde", "Jorge"))
print(executa(saudacao, "Boa noite", "Gabriel"))