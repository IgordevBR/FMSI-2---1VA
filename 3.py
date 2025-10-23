def exponencial_modular(a, n, m):
    #caso invalido
    if m <= 1:
        return "impossível calcular"
    if a == 0 and n == 0:
        return "impossível calcular"

    #caso base
    if n == 0:
        return 1 % m

    #caso base
    if n == 1:
        return a % m

    #recursividade
    if n % 2 == 0:
        meio = exponencial_modular(a, n // 2, m)
        return (meio * meio) % m
    else:
        return (a % m) * exponencial_modular(a, n - 1, m) % m


#entrada do usuario
while True:
    try:
        a = int(input("digite a base: "))
        n = int(input("digite o expoente inteiro e maior que 0: "))
        m = int(input("digite o modulo inteiro e maior que 2: "))

        if n < 0:
            print("erro: o expoente deve ser um numero inteiro > ou = a zero.\n")
            continue

        resultado = exponencial_modular(a, n, m)
        print(f"{resultado}")
        break

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.\n")
