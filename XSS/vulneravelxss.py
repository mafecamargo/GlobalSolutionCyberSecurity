
# Comentário do usuário é exibido sem sanitização
comentario = input("Digite seu comentário: ")
html = f"<div>{comentario}</div>"  # Se comentário = <script>alert('XSS');</script>
print(html)
