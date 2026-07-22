import sqlite3

# Conecta (ou cria) o banco loja.db
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL
)
""")

# Insere 3 produtos
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Notebook", 2500.00))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Mouse", 50.00))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Teclado", 120.00))

conexao.commit()
conexao.close()

print("Banco de dados 'loja.db' criado com sucesso!")
print("3 produtos inseridos.")
