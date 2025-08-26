#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:

#a) o maior número da lista

numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}° número:"))
    numeros.append(num)
print("\nLista de números digitados:", numeros)
print("O maior número da lista é:", max(numeros))

#b) o menor número da lista

numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}° número:"))
    numeros.append(num)
print("\nLista de números digitados:", numeros)
print("O menor número da lista é:", min(numeros))

#c) a média dos números contidos na lista


numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}° número:"))
    numeros.append(num)
print("\nLista de números digitados:", numeros)
media = sum(numeros) / len(numeros)
print("A média dos números da lista é:", media)
