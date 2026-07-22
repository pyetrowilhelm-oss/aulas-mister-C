from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de produtos em memória
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "disponivel": True}
]

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo = request.get_json()
    produtos.append(novo)
    return jsonify(novo), 201

if __name__ == "__main__":
    app.run(debug=True)
