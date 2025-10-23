def mdc(a, b):
    #caso especial
    if a == 0 and b == 0:
        return "indeterminado"
    
    #caso base
    if b == 0:
        return abs(a)
    
    #recursividade
    return mdc(b, a % b)


#entrada do usuario
while True:
    try:
        a = int(input("Digite o primeiro numero inteiro: "))
        b = int(input("Digite o segundo numero inteiro: "))
        
        resultado = mdc(a, b)
        print(f"{resultado}")
        break

    except ValueError:
        print("Entrada invalida. Digite apenas numeros inteiros.\n")
