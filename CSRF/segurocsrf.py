# Verificação com token CSRF
if request.method == "POST" and request.form["csrf_token"] == session["csrf_token"]:
    usuario.senha = request.form["novaSenha"]