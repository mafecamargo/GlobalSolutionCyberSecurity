
# Qualquer POST altera a senha sem verificação
if request.method == "POST":
    usuario.senha = request.form["novaSenha"]
