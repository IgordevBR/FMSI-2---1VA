def exponencial(a, n):
    #caso especial
    if a == 0 and n == 0:
        return "impossível calcular"
    
    #caso base
    if n == 0:
        return 1
    
    #caso base
    if n == 1:
        return a
    
    #recursividade
    return a * exponencial(a, n - 1)


#entrada do usuario
while True:
    try:
        a = float(input("digite o número base: "))
        n = int(input("digite o expoente (inteiro e = ou > 0): "))
        
        if n < 0:
            print("erro: o expoente deve ser um número inteiro maior ou igual a zero.\n")
            continue

        resultado = exponencial(a, n)
        print(f"{resultado}")
        break
        
    #tratamento de erro   
    except ValueError:
        print("Entrada inválida. Digite um número válido para a base e o expoente.\n")
