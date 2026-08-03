from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).parent / "marmitaria.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marmitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias")
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados), 200


@app.route("/categorias/<int:id>", methods=["GET"])
def obter_categoria(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({"erro": "Categoria não encontrada"}), 404
    return jsonify(dict(row)), 200


@app.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.get_json()

    if not dados or not dados.get("nome"):
        return jsonify({"erro": "Campo nome é obrigatório"}), 400

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO categorias (nome, descricao) VALUES (?, ?)",
            (dados["nome"], dados.get("descricao"))
        )
        conn.commit()
        novo_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Categoria já existe"}), 400

    conn.close()
    return jsonify({"id": novo_id, "mensagem": "Categoria criada"}), 201


@app.route("/categorias/<int:id>", methods=["PUT"])
def atualizar_categoria(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM categorias WHERE id = ?", (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor.execute(
        "UPDATE categorias SET nome = ?, descricao = ? WHERE id = ?",
        (dados.get("nome"), dados.get("descricao"), id)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Categoria atualizada"}), 200


@app.route("/categorias/<int:id>", methods=["DELETE"])
def deletar_categoria(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM categorias WHERE id = ?", (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Categoria deletada"}), 200


@app.route("/marmitas", methods=["GET"])
def listar_marmitas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM marmitas")
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados), 200


@app.route("/marmitas/<int:id>", methods=["GET"])
def obter_marmita(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM marmitas WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return jsonify({"erro": "Marmita não encontrada"}), 404
    return jsonify(dict(row)), 200


@app.route("/marmitas", methods=["POST"])
def criar_marmita():
    dados = request.get_json()

    if not dados or not dados.get("nome") or "preco" not in dados or "categoria_id" not in dados:
        return jsonify({"erro": "Campos nome, preco e categoria_id são obrigatórios"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM categorias WHERE id = ?", (dados["categoria_id"],))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 400

    cursor.execute(
        "INSERT INTO marmitas (nome, descricao, preco, categoria_id) VALUES (?, ?, ?, ?)",
        (dados["nome"], dados.get("descricao"), dados["preco"], dados["categoria_id"])
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": novo_id, "mensagem": "Marmita criada"}), 201


@app.route("/marmitas/<int:id>", methods=["PUT"])
def atualizar_marmita(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM marmitas WHERE id = ?", (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Marmita não encontrada"}), 404

    cursor.execute(
        "UPDATE marmitas SET nome = ?, descricao = ?, preco = ?, categoria_id = ? WHERE id = ?",
        (dados.get("nome"), dados.get("descricao"), dados.get("preco"), dados.get("categoria_id"), id)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Marmita atualizada"}), 200


@app.route("/marmitas/<int:id>", methods=["DELETE"])
def deletar_marmita(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM marmitas WHERE id = ?", (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Marmita não encontrada"}), 404

    cursor.execute("DELETE FROM marmitas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Marmita deletada"}), 200


@app.route("/marmitas/com-categoria", methods=["GET"])
def marmitas_com_categoria():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.id, m.nome, m.descricao, m.preco, m.categoria_id, c.nome AS categoria_nome
        FROM marmitas m
        INNER JOIN categorias c ON m.categoria_id = c.id
    """)
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados), 200


@app.route("/categorias/<int:id>/marmitas", methods=["GET"])
def marmitas_por_categoria(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM categorias WHERE id = ?", (id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor.execute("SELECT * FROM marmitas WHERE categoria_id = ?", (id,))
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados), 200


@app.route("/marmitas/busca", methods=["GET"])
def buscar_marmitas():
    nome = request.args.get("nome")

    if not nome:
        return jsonify({"erro": "Parâmetro nome é obrigatório"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM marmitas WHERE nome LIKE ?", (f"%{nome}%",))
    dados = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(dados), 200


if __name__ == "__main__":
    init_db()
    print("API rodando em http://127.0.0.1:5000")
    app.run(debug=True)