from datetime import date
from pathlib import Path
from database import (consultar_tarefas, inserir_tarefa, buscar_tarefa, concluir_tarefa, apagar_tarefa)

from flask import Flask, render_template, redirect, session, request, flash

CATEGORIAS = ["Escola", "Trabalho", "Projetos", "Pessoal", "Saúde", "Outros"]
app = Flask(__name__)
app.secret_key = "moroni"

# Dados de acesso do ADMIN
ADMIN_EMAIL = "moroni@gmail.com"
ADMIN_SENHA = "123456"

#-----------------------------------------------------------------------
# Validar tarefas
def validar_tarefa(nome, descricao, categoria, prazo, prioridade):
    erros = []
    if len(nome) < 5 or len(nome) > 30 or nome.isdigit() : # Se o nome tiver meno que 5 ou mais de 30 caracteres, Ou só números...
        erros.append("Nome: de 5 a 30 caracteres, não só números")
    if len(descricao) > 100: # Se a descrição tiver mais de 100 caracteres...
        erros.append("Descrição: no máximo 100 caracteres.")
    if len(categoria) < 5 or len(categoria) > 30 or categoria.isdigit():
        erros.append("Categoria: de 5 a 30 caracteres, não só números")
    if prioridade not in ("ALTA", "MEDIA", "BAIXA"):
        erros.append("Prioridade inválida.")

    # Validar o prazo aqui
    try:
        data = date.fromisoformat(prazo)
        if data < date.today():
            erros.append("Prazo: a data não pode ser no passado.")
    except ValueError:
        erros.append("Prazo: informe uma dara válida")

    return erros

#-----------------------------------------------------------------------
# HomePage- Página Inicial
@app.route("/") # "@app.route (/)" -> informa a rota
def home(): # Função para ir até a página ("index.html")
    if "login" not in session: # Se a pessoa não estiver logada -> redireciona para a página de login 
        return redirect("/login")

    # Se o usuário estiver logado -> retorna à página ("index.html")
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
# Criar tarefas no Banco
@app.route("/adicionar", methods=["GET", "POST"]) 
def adicionar(): # Adicionar tarefas
    if request.method == "GET": # Se o método for GET --> renderiza a página ("formulários.html") para adicionar as tarefas
        return render_template("formularios.html", categorias=CATEGORIAS, dados={}, erros=[])

    # Após renderizar a página, deve-se mandar as informações para o banco de dados pelo formulário
    # POST: ler o que veio do formulário
    # O Banco de dados atualiza cada variável para uma nova variável 
    nome_tarefa = request.form.get("nome_tarefa", "").strip
    descricao = request.form.get("descricao", "").strip
    categoria = request.form.get("categoria", "").strip
    data_prazo = request.form.get("data_prazo", "").strip
    prioridade = request.form.get("prioridade", "").strip

    # Validar os Campos aqui
    erros = validar_tarefa(nome_tarefa, descricao, categoria, data_prazo, prioridade) # 

    if erros:
        return render_template("formulario.html", categorias=CATEGORIAS, dados=request.form, erros=erros)
    
    # Gravar no Banco
    if inserir_tarefa(nome_tarefa, descricao, categoria, data_prazo, prioridade):
        flash("Tarefa adicionada com sucesso!")
    else:
        flash("Não foi possível salvar. Confira a conexão com o banco")
    return redirect("/")

# --------------------------------------
# Concluir tarefa
@app.route("/concluir/<int:idtarefa>", methods=["POST"])
def concluir(idtarefa): # Concluir tarefa
    tarefa = buscar_tarefa(idtarefa)
    if tarefa is None or tarefa["status"] == "Concluída":
        flash("Não há o que concluir nessa tarefa.")
    elif concluir_tarefa(idtarefa):
        flash("Tarefa concluída. Bom trabalho!")
    else:
        flash("Não foi posível concluir a tarefa.")
    return redirect("/")







if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # host='0.0.0.0' Habilita o IP Público








