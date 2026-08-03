from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("marmitaria.db")
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT
        )
    """)
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS marmitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
        )
    """)
    conexao.commit()
    conexao.close()


@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM categorias")
    categorias = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(categorias)

@app.route("/categorias/<int:id>", methods=["GET"])
def obter_categoria(id):
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM categorias WHERE id = ?", (id,))
    categoria = cursor.fetchone()
    conexao.close()

    if not categoria:
        return jsonify({"erro": "Categoria nao encontrada"}), 404
    return jsonify(dict(categoria))

@app.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.get_json()

    if not dados or "nome" not in dados:
        return jsonify({"erro": "O campo nome e obrigatorio"}), 400

    conexao = conectar()
    try:
        cursor = conexao.execute(
            "INSERT INTO categorias (nome, descricao) VALUES (?, ?)",
            (dados["nome"], dados.get("descricao"))
        )
        conexao.commit()
        novo_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conexao.close()
        return jsonify({"erro": "Categoria ja existe"}), 400

    conexao.close()
    return jsonify({"id": novo_id, **dados}), 201

@app.route("/categorias/<int:id>", methods=["PUT"])
def atualizar_categoria(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados invalidos"}), 400

    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE categorias SET nome = ?, descricao = ? WHERE id = ?",
        (dados.get("nome"), dados.get("descricao"), id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Categoria nao encontrada"}), 404
    return jsonify({"id": id, **dados})

@app.route("/categorias/<int:id>", methods=["DELETE"])
def deletar_categoria(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Categoria nao encontrada"}), 404
    return jsonify({"mensagem": "Categoria deletada"})


@app.route("/marmitas", methods=["GET"])
def listar_marmitas():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM marmitas")
    marmitas = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(marmitas)

@app.route("/marmitas/<int:id>", methods=["GET"])
def obter_marmita(id):
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM marmitas WHERE id = ?", (id,))
    marmita = cursor.fetchone()
    conexao.close()

    if not marmita:
        return jsonify({"erro": "Marmita nao encontrada"}), 404
    return jsonify(dict(marmita))

@app.route("/marmitas", methods=["POST"])
def criar_marmita():
    dados = request.get_json()

    if not dados or "nome" not in dados or "preco" not in dados or "categoria_id" not in dados:
        return jsonify({"erro": "Campos nome, preco e categoria_id sao obrigatorios"}), 400

    conexao = conectar()

    cursor = conexao.execute("SELECT id FROM categorias WHERE id = ?", (dados["categoria_id"],))
    if not cursor.fetchone():
        conexao.close()
        return jsonify({"erro": "Categoria nao encontrada"}), 400

    cursor = conexao.execute(
        "INSERT INTO marmitas (nome, descricao, preco, categoria_id) VALUES (?, ?, ?, ?)",
        (dados["nome"], dados.get("descricao"), dados["preco"], dados["categoria_id"])
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, **dados}), 201

@app.route("/marmitas/<int:id>", methods=["PUT"])
def atualizar_marmita(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados invalidos"}), 400

    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE marmitas SET nome = ?, descricao = ?, preco = ?, categoria_id = ? WHERE id = ?",
        (dados.get("nome"), dados.get("descricao"), dados.get("preco"), dados.get("categoria_id"), id)
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Marmita nao encontrada"}), 404
    return jsonify({"id": id, **dados})

@app.route("/marmitas/<int:id>", methods=["DELETE"])
def deletar_marmita(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM marmitas WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Marmita nao encontrada"}), 404
    return jsonify({"mensagem": "Marmita deletada"})


@app.route("/marmitas/com-categoria", methods=["GET"])
def marmitas_com_categoria():
    conexao = conectar()
    cursor = conexao.execute("""
        SELECT m.id, m.nome, m.descricao, m.preco, m.categoria_id, c.nome AS categoria_nome
        FROM marmitas m
        INNER JOIN categorias c ON m.categoria_id = c.id
    """)
    resultado = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(resultado)


@app.route("/categorias/<int:id>/marmitas", methods=["GET"])
def marmitas_por_categoria(id):
    conexao = conectar()

    cursor = conexao.execute("SELECT id FROM categorias WHERE id = ?", (id,))
    if not cursor.fetchone():
        conexao.close()
        return jsonify({"erro": "Categoria nao encontrada"}), 404

    cursor = conexao.execute("SELECT * FROM marmitas WHERE categoria_id = ?", (id,))
    marmitas = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(marmitas)

@app.route("/marmitas/busca", methods=["GET"])
def buscar_marmitas():
    nome = request.args.get("nome")

    if not nome:
        return jsonify({"erro": "Parametro nome e obrigatorio"}), 400

    conexao = conectar()
    cursor = conexao.execute(
        "SELECT * FROM marmitas WHERE nome LIKE ?",
        (f"%{nome}%",)
    )
    marmitas = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(marmitas)

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)
