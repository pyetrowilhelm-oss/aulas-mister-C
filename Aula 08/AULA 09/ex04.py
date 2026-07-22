from flask import Flask, jsonify

app = Flask(__name__)

# Lista de produtos
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 2500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse", "preco": 50.00, "disponivel": True},
    {"id": 3, "nome": "Teclado", "preco": 120.00, "disponivel": False},
    {"id": 4, "nome": "Monitor", "preco": 800.00, "disponivel": True}
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/disponiveis")
def produtos_disponiveis():
    disponiveis = [p for p in produtos if p["disponivel"]]
    return jsonify(disponiveis)

if __name__ == "__main__":
    app.run(debug=True)
