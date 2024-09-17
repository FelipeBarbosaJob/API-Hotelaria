import sqlite3

connection = sqlite3.connect(r'C:\Users\felip\OneDrive\Documentos\Projetos\REST_API\banco.db')
cursor = connection.cursor()

criar_tabela = """
CREATE TABLE IF NOT EXISTS hoteis (
    hoteis_id TEXT PRIMARY KEY UNIQUE NOT NULL,
    nome TEXT,
    estrelas REAL,
    diaria REAL,
    cidade TEXT
)
"""
cursor.execute(criar_tabela)

# Insere um hotel na tabela
criar_hotel = """
INSERT INTO hoteis (hoteis_id, nome, estrelas, diaria, cidade)
VALUES ('101', 'Hotel Paraíso', 5, 350.00, 'Rio de Janeiro')
"""
cursor.execute(criar_hotel)
connection.commit()
connection.close()
