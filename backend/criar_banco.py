import sqlite3
import os
from main import figurinhas

# Define database name and path
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(PASTA_BASE, "banco_album.sqlite")

def inicializar_banco():
    print(f"Criando e populando o banco de dados em: {DB_PATH}")
    
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Cria a tabela figurinhas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS figurinhas (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        imagem_url TEXT NOT NULL,
        descricao TEXT NOT NULL,
        brasil INTEGER NOT NULL
    )
    """)
    
    # Insere as figurinhas do main.py
    for fig in figurinhas:
        cursor.execute("""
        INSERT OR REPLACE INTO figurinhas (id, nome, categoria, imagem_url, descricao, brasil)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            fig["id"],
            fig["nome"],
            fig["categoria"],
            fig["imagem_url"],
            fig["descricao"],
            1 if fig["brasil"] else 0
        ))
        
    conn.commit()
    conn.close()
    print("Banco de dados criado e populado com sucesso!")

if __name__ == "__main__":
    inicializar_banco()
