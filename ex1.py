#EXERCÍCIOS - STRINGS, LISTAS E TUPLAS

#Escreva uma função que receba uma string e retorne o número de caracteres nela.

def caractere(texto):
    texto = len(texto)
    print(f"A quantidade de caracteres da palavra é: {texto}")
texto = input("Digite a palavra: ")

caractere(texto)
