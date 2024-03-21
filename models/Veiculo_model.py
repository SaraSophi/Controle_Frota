from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, VARCHAR, CHAR, SMALLINT, DATE, NUMERIC, ForeignKey

Base = declarative_base()

class Veiculo(Base):
    __tablename__ = "VEICULO"

    idVeic        = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    nrPlaca       = Column(CHAR(7), nullable=False, unique=True)
    dsModelo      = Column(VARCHAR(100), nullable=False)
    tpTracao      = Column(VARCHAR(40), nullable=False)
    nrRenavam     = Column(NUMERIC(11), nullable=False, unique=True)
    dtAquisicao   = Column(DATE, nullable=False)
    nrFrota       = Column(NUMERIC(5), nullable=True)
    nrConjunto    = Column(NUMERIC(5), nullable=True)
    nrChassi      = Column(VARCHAR(17), nullable=False, unique=True)
    tpCombustivel = Column(VARCHAR(100))
    anoVeic       = Column(NUMERIC(4), nullable=False)
    dsMarca       = Column(VARCHAR(100), nullable=False)
    qtEixo        = Column(SMALLINT, nullable=False)

    tpVeic          = Column(CHAR(1),  ForeignKey('tpVeiculo.idTpVeic'))
    tpOperacao      = Column(CHAR(1), ForeignKey('Operacao.idOperacao'))
    tpClassificacao = Column(CHAR(1),  ForeignKey('Classificacao.idClassificacao'))

    Operacao        = relationship("Operacao")
    Classificacao   = relationship("Classificacao")
    tpVeiculo       = relationship("tpVeiculo")




'''
Antes
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR, SMALLINT, DATE
from models import Base

class Veiculo(Base):
    __tablename__ = "VEICULO"
    idVeic:        Mapped[int] = mapped_column(Integer,     nullable=False, autoincrement=True, primary_key=True)
    nrPlaca:       Mapped[str] = mapped_column(CHAR(7),     nullable=False, unique=True)
    dsModelo:      Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    tpTracao:      Mapped[str] = mapped_column(VARCHAR(40), nullable=False)
    nrRenavam:     Mapped[int] = mapped_column(Integer(11), nullable=False, unique=True)
    dtAquisicao:   Mapped[DATE]= mapped_column(DATE,        nullable=False)
    nrFrota:       Mapped[int] = mapped_column(Integer(5),  nullable=True)
    nrConjunto:    Mapped[int] = mapped_column(Integer(5),  nullable=True)
    nrChassi:      Mapped[str] = mapped_column(VARCHAR(17), nullable=False, unique=True)
    tpCombustivel: Mapped[str] = mapped_column(VARCHAR(100))
    anoVeic:       Mapped[int] = mapped_column(SMALLINT,    nullable=False)
    dsMarca:       Mapped[str] = mapped_column(VARCHAR(100),nullable=False)
    qtEixo:        Mapped[int] = mapped_column(SMALLINT,    nullable=False)

'''