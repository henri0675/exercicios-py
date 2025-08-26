#Crie uma função que retorne a quantidade de vogais (a, e, i, o, u) existentes em uma string

def vogal(texto):
    cont = 0
    for x in texto:
        if x.lower() == "a" or x.lower() == "e" or x.lower() == "i" or x.lower() == "o" or x.lower() == "u":
            cont += 1
    return cont
texto = input("Digite uma palavra: ")

print(vogal(texto))