from models.Classificacao import Classificacao
from utils.create_db import create_db
from services.db import session

if __name__ == "__main__":
    """create_db()"""
    print("Teste")

    response = session.query(Classificacao)

    for classificacao in response:
        print(classificacao.IDCLASSIFICACAO)
        print(classificacao.DSCLASSIFICACAO)
