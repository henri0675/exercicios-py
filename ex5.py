#Implemente uma função que retorne a quantidade de palavras existentes em uma string.

def contador_palavras():
    frase = input("Digite uma frase:")
    palavras = frase.split()
    return len(palavras)
print("Quantidade de palavras presentes na string:", contador_palavras())