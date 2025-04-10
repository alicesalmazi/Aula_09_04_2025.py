texto = input("Digite uma frase: ")

palavras = texto.split(" ")

hashtag_1 = ""
for i in range(len(palavras)):
    if len(palavras[i]) >= 5:
        hashtag_1 += f"#{palavras[i].capitalize()} "

print(hashtag_1)