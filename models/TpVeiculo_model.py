from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, VARCHAR, Column, NUMERIC

Base = declarative_base()
class TpVeiculo(Base):
    __tablename__  = "TPVEICULO"
    idTpVeiculo    = Column(NUMERIC,       nullable=False, autoincrement=True, primary_key=True)
    dsTpVeiculo    = Column(VARCHAR(100), nullable=False)
   

