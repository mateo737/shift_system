def numeros_perfumeria():
    for i in range(1,10000):
        yield f"P - {i}"

def numeros_farmacia():
    for i in range(1,10000):
        yield f"F - {i}"

def numeros_cosmetca():
    for i in range(1,10000):
        yield f"C - {i}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetca()

def decorador(rubro):

    print("\n" + "*"*23)
    print("Su numero es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Espera y sera atendido")
    print("*"*23 + "\n")
    