from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas em memória
tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova = request.get_json()
    
    # Validação: título não pode ser vazio
    if not nova or "titulo" not in nova or not nova["titulo"].strip():
        return jsonify({"erro": "O titulo e obrigatorio e nao pode ser vazio"}), 400
    
    tarefas.append(nova)
    return jsonify(nova), 201

if __name__ == "__main__":
    app.run(debug=True)
