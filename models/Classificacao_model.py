from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, VARCHAR, Column, NUMERIC

Base = declarative_base()
class Classificacao(Base):
    __tablename__   = "Classificacao"
    idClassificacao = Column(NUMERIC,        nullable=False, autoincrement=True, primary_key=True)
    dsClassificacao = Column(VARCHAR(100), nullable=False)

  
