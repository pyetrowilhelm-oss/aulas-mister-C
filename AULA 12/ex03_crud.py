from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            feita INTEGER DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM tarefas")
    tarefas = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova = request.get_json()
    if not nova or "titulo" not in nova or not nova["titulo"].strip():
        return jsonify({"erro": "O titulo e obrigatorio e nao pode ser vazio"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO tarefas (titulo, feita) VALUES (?, ?)",
        (nova["titulo"], nova.get("feita", 0))
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, **nova}), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados invalidos"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE tarefas SET titulo = ?, feita = ? WHERE id = ?",
        (dados.get("titulo"), dados.get("feita"), id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    
    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404
    return jsonify({"id": id, **dados})

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar_tarefa(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    
    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404
    return jsonify({"mensagem": "Tarefa apagada com sucesso"})

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
