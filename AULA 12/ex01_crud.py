from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("loja.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM produtos")
    produtos = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo = request.get_json()
    if not novo or "preco" not in novo:
        return jsonify({"erro": "O campo preco e obrigatorio"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (novo.get("nome"), novo["preco"])
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, **novo}), 201

# UPDATE - PUT
@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados invalidos"}), 400
    
    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?",
        (dados.get("nome"), dados.get("preco"), id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()
    
    if afetadas == 0:
        return jsonify({"erro": "Produto nao encontrado"}), 404
    return jsonify({"id": id, **dados})

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
