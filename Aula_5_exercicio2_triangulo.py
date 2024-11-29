# Recebimento dos lados do triângulo

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Verificar se realmente é um triângulo

verifica_triangulo = a + b > c and b + c > a and c + a > b

if verifica_triangulo:
    print(f"{a}, {b}, {c} forma um triângulo do tipo: ", end="")
    # Verificando se é equilátero
    if a == b == c:
        print("Equilátero.")

    # Isóceles
    elif a == b or b == c or c == a:
        print("Isóceles.")

    elif a != b != c:
        print("Escaleno.")

    else:
        pass
else:
    print(f"{a}, {b}, {c} não forma um triângulo.")