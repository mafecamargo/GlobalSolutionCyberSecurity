
# Escapar caracteres HTML
import html


comentario = input("Digite seu comentário: ")
comentario_seguro = html.escape(comentario)
html = f"<div>{comentario_seguro}</div>"
print(html)
