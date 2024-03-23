from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, VARCHAR, CHAR, Column

Base = declarative_base()
class Uf():
    __tablename__ = "UF"
    cdUf          = Column(Integer,      nullable=False, autoincrement=True, primary_key=True)
    nmUf          = Column(VARCHAR(100), nullable=False)
    dsSigla       = Column(CHAR(2),      nullable=False)