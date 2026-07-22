import sqlite3

# Conecta ao banco
conexao = sqlite3.connect("loja.db")
conexao.row_factory = sqlite3.Row  # Para retornar como dicionário
cursor = conexao.cursor()

# Busca todos os produtos
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

print("Produtos cadastrados:")
for produto in produtos:
    print(dict(produto))

conexao.close()
