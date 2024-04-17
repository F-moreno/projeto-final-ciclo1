# AVISO: ESSE ARQUIVO DELETA E RECRIA TODAS AS TABELAS DO BANCO DE DADOS 'db_projeto'
# PERDE TODOS OS REGISTROS

from .bd_classes import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Tabelas atualizadas com sucesso.")
