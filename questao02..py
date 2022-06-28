
numero = int(input("Digite um numero: "))
ultimo = 1
penultimo = 0
fib = 0
count = 1

while (count <= numero):
    fib = ultimo + penultimo
    penultimo = ultimo
    ultimo = fib
    count += 1
    if(fib == numero):
        print("Está")
        break

if(fib != numero):
    print("Não está")
