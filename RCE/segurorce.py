# Permitir apenas comandos pré-definidos
comando = input("Digite um comando permitido: ")
comandos_permitidos = ["ls", "pwd"]
if comando in comandos_permitidos:
    os.system(comando)
else:
    print("Comando não permitido!")