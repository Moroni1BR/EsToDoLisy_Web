from flask import Flask, render_template, request, session, redirect
from database import consultar_tarefas

app = Flask(__name__)
app.secret_key = "moroni"

# Dados de acesso do ADMIN
ADMIN_EMAIL = "moroni@gmail.com"
ADMIN_SENHA = "123456"

# HomePage- Página Inicial
@app.route("/") # "@app.route (/)" -> informa a rota
def home(): # Função para ir até a página ("index.html")
    if "login" not in session: # Se a pessoa não estiver logada -> redireciona para a página de login 
        return redirect("/login")

    # Se o usuário estiver logado -> retorna à página de login
    tarefas = consultar_tarefas()
    return render_template("index.html", tarefas = tarefas) # "tarefas = tarefas -> ao passar a variável (tarefa) para o index.html, deve se criar outra variável, ex: tarefas (variável do index) = tarefas (variável do app.py)"

# -----------------------------------------
# LoginPage - Página de Login
@app.route("/login", methods=["GET","POST"]) # A página de Login usa os dois tipos de métodos ["GET" e "POST"]
def login(): # Função para ir até a página ("login.html")
    if "login" in session: # Se o 
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")
   
    # POST
    email = request.form.get("email") # Pegando o email que estava no form HTML
    senha = request.form.get("senha") # Essa informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True # Cria a sessão login
        return redirect("/") # Redireciona para a rota inicial
    else:
        return render_template("login.html", msgerro = "E-mail ou senha estão incorretos!")

# ----------------------
# Rota Logout
@app.route("/logout")
def logout():
    session.clear() # Apaga a lista sessão
    return redirect("/login")

# --------------------------------------
# Tratamento de erro - Código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")

# --------------------------------------
# Buscar tarefas no Banco






if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # host='0.0.0.0' Habilita o IP Público








