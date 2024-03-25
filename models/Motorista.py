from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR, ForeignKey
from models.Base import Base
from models.Pessoa import Pessoa
class Motorista(Base):
    __tablename__ = "MOTORISTA"
    IDMOTORISTA:   Mapped[int]      = mapped_column(INTEGER,      nullable=False, primary_key=True)
    NMMOTORISTA:   Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    TPSITUACAO:    Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    IDPESSOA:      Mapped[int]      = mapped_column(INTEGER, ForeignKey(Pessoa.IDPESSOA), nullable=False)