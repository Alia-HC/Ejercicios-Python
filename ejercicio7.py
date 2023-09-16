def primos(x, y):
    lista = []
    for n in range(x, y):
        primo = True

        for num in range(2, n):
            if n % num == 0:
                primo = False

        if primo:
            lista.append(n)
            
    return lista

print(primos(150, 350))