print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)   # faz a divisao e mostra o resultado inteiro
print(5 % 2)  # mostra o resto da divisao
print(5 ** 0.5) # para fazer a raiz quadrada de um numero 

'''
Ordem de precência
1 - ()
2 - **
3 - *, /, //, %
4 - +, - 
'''
# Exemplos:
print(5+3*2)  # = 11
print(3*5+4**2)  # = 31
print(3*(5+4)**2)  # = 243
print('-'*100)

nome = input("Digite o seu nome: ")
print("Prazer em te conhecer {:=^20}".format(nome))

n1 = float(input("Digite um valor: ").replace(",", "."))
n2 = float(input("Digite outro valor: ").replace(",", "."))

multiplicacao = round(n1 * n2, 2)
elevacao = round(n1 ** n2, 2)
divisao = round(n1 / n2, 2)
divisaoInteira = (n1 // n2, 2)

print(f"A soma é {soma}, a multiplicação é {multiplicacao}, a elevação é {elevacao}, \
a divisão é {divisao} e a divisão inteira {divisaoInteira}")
