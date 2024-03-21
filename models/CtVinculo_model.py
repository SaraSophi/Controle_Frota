from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, DATE, ForeignKey, Column, NUMERIC
Base = declarative_base()

class CtVinculo_model(Base):
    __tablename__     = "CTVINCULO"
    id                = Column(Integer, nullable=False, primary_key=True,autoincrement=True)
    dtVinculo         = Column(DATE,    nullable=False)
    dtDesvinculo      = Column(DATE,    nullable=True)
    motoristaIdMotora = Column(Integer, ForeignKey('Motorista_model.idMotora'))
    veiculoIdVeic     = Column(Integer, ForeignKey('Veiculo_model.idVeic'))
    nrFrota          = Column(NUMERIC(5), nullable=True)

    Motorista = relationship('Motorista')
    veiculo   = relationship("Veiculo")

