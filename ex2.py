#Crie uma função que receba uma string e retorne a mesma string com todas as letras em maiúsculas

def maiuscula(texto):
    texto = texto.upper()
    return texto
texto = input("Digite uma palavra:")

print (maiuscula(texto))