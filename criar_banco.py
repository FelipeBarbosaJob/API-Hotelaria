import sqlite3

connection = sqlite3.connect(r'C:\Users\felip\OneDrive\Documentos\Projetos\REST_API\banco.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis  (hoteis_id texto PRIMARY KEY UNIQUE NOT NULL, nome text, estrelas real, diaria real, cidade text)"
criar_hotel = "INSERT INTO hoteis VALEUS (101,Hotel Paraíso,5,350.00, Rio de Janeiro )"
cursor.execute(criar_tabela)
cursor.execute(criar_hotel)

connection.commit()
connection.close()
