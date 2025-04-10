def validarEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem).strip())
            return valor
        except ValueError:
            print("Digite um valor válido!")

def calculoAreaRetangulo(lado, base):
    area = lado * base
    print(f"O retângulo de lado = {lado} e base = {base} tem área = {area}")
    

lado = validarEntrada("Digite o valor do lado do retângulo: ")
base = validarEntrada("Digite o valor da base do retângulo: ")
calculoAreaRetangulo(lado, base)