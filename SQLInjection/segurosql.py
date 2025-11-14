# Exemplo vulnerável
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# Consulta insegura
query = "SELECT * FROM usuarios WHERE nome = ? AND senha = ?"