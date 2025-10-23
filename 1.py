def fatorial(n):
    #caso base
    if n < 0:
        return 0
    
    #caso base
    if n == 0 or n == 1:
        return 1
    
    #recursividade
    return n * fatorial(n - 1)

#entrada do usuário
while True:
    
    entrada = input("Digite um número inteiro para calcular seu valor fatorial através da recursividade: ")

    if entrada.lstrip('-').isdigit():  #verifica se 'n' é inteiro (positivo ou negativo)
        n = int(entrada)
        print(f"{n}! = {fatorial(n)}")
        break

    #tratamento de erro caso a entrada não seja um número inteiro
    else:
        print("Erro: digite apenas um número inteiro válido")
