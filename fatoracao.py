def fatoracao(numero):
    fatores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return fatores

# Número que queremos fatorar
numero = 1024

# Chamando a função e imprimindo a fatoração
fatores = fatoracao(numero)

# Imprimindo os fatores
print(f"Fatoração de {numero}: {fatores}")
