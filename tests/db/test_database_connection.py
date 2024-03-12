"""
Copyright (c) J-Tech Solucoes em Informatica.
All Rights Reserved.

This software is the confidential and proprietary information of J-Tech.
("Confidential Information"). You shall not disclose such Confidential
Information and shall use it only in accordance with the terms of the
license agreement you entered into with J-Tech.
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Substitua com sua própria string de conexão ao banco de dados
DATABASE_URI = "sqlite:///./test.db"  # Exemplo para SQLite


def test_database_connection():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)

    try:
        # Tenta criar uma sessão e conectar ao banco de dados
        session = Session()
        # Se esta linha for executada sem erros, significa que a conexão foi estabelecida com sucesso
        session.execute('SELECT 1')
        return True
    except SQLAlchemyError as e:
        # Se houver um erro, ele será impresso e o teste retornará False
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False
    finally:
        # Fecha a sessão se ela foi aberta
        session.close()
        # Descarta o engine, que libera a conexão de volta ao pool
        engine.dispose()


# Executa o teste de conexão
if test_database_connection():
    print("Conexão com o banco de dados foi estabelecida com sucesso.")
else:
    print("Falha ao estabelecer conexão com o banco de dados.")

