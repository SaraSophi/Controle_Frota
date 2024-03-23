from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Integer, DATE, ForeignKey, Column, NUMERIC
Base = declarative_base()

class CtVinculo_model(Base):
    __tablename__     = "CTVINCULO"
    id                = Column(NUMERIC,  nullable=False, primary_key=True,autoincrement=True)
    dtVinculo         = Column(DATE,    nullable=False)
    dtDesvinculo      = Column(DATE,    nullable=True)
    nrFrota = Column(NUMERIC(5),         nullable=True)

    motoristaIdMotora = Column(NUMERIC, ForeignKey('Motorista_model.idMotora'))
    veiculoIdVeic     = Column(NUMERIC, ForeignKey('Veiculo_model.idVeic'))

    Motorista = relationship('Motorista')
    veiculo   = relationship("Veiculo")

