import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 titulo TEXT,
 autor TEXT,
 emprestado INTEGER,
 aluno TEXT
)
""")

conexao.commit()

conexao.close()

print("Banco criado com sucesso")