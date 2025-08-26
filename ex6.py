#Escreva uma função que remova todos os espaços em branco de uma string e retorne a string resultante

def removedor_espaco():
    frase = input("Digite uma frase: ")
    frase_sem_espaco = frase.replace(" ", "")
    return frase_sem_espaco
print("A string resultante sem espaços em branco é:", removedor_espaco())