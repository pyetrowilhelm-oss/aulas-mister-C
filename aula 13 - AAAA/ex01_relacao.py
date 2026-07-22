import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

def criar_tabelas():
    conexao = conectar()
    
    # Tabela autores
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)
    
    # Tabela livros com chave estrangeira
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)
    
    conexao.commit()
    conexao.close()

def inserir_dados():
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Autores
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", ("Machado de Assis",))
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", ("Clarice Lispector",))
    
    # Livros
    cursor.execute("INSERT INTO livros (titulo, autor_id) VALUES (?, ?)", ("Dom Casmurro", 1))
    cursor.execute("INSERT INTO livros (titulo, autor_id) VALUES (?, ?)", ("Memórias Póstumas de Brás Cubas", 1))
    cursor.execute("INSERT INTO livros (titulo, autor_id) VALUES (?, ?)", ("A Hora da Estrela", 2))
    
    conexao.commit()
    conexao.close()
    print("Banco 'biblioteca.db' criado com autores e livros relacionados.")

if __name__ == "__main__":
    criar_tabelas()
    inserir_dados()
