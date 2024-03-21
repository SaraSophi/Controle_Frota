from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, DATE, ForeignKey, Column, NUMERIC

Base = declarative_base()

class CtEngate(Base):
    __tablename__ = "CTENGATE"
    id            = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    dtEngate      = Column(DATE, nullable=False)
    dtDesengat    = Column(DATE, nullable=True)
    nrFrota       = Column(NUMERIC(5), nullable=True)
    veiculoIdVeic = Column(Integer, ForeignKey('Veiculo_model.idVeic'))

    veiculo = relationship("Veiculo")