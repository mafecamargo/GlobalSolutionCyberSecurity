
# Exemplo vulnerável
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# Consulta insegura
query = f"SELECT * FROM usuarios WHERE nome = '{usuario}' AND senha = '{senha}'"
cursor.execute(query)  # Se usuario = 'admin' --, ignora senha e acessa conta
