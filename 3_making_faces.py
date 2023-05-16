def carinhas(texto):
    texto = texto.replace(":)", "🙂")
    texto = texto.replace(":(", "🙁")
    return texto

def main():
    texto = input("Digite algo:")
    texto_modificado = carinhas(texto)
    print("Texto modificado:", texto_modificado)
main()