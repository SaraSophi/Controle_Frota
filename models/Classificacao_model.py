from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, VARCHAR, Column

Base = declarative_base()
class Classificacao(Base):
    __tablename__   = "Classificacao"
    idClassificacao = Column(Integer,     nullable=False, autoincrement=True, primary_key=True)
    dsClassificacao = Column(VARCHAR(100),nullable=False)

  
