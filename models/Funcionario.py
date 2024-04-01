from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, DATE, VARCHAR, CHAR, ForeignKey
from models.Base import Base
from datetime import datetime
from models.Pessoa import Pessoa
class Funcionario(Base):
    __tablename__ = "FUNCIONARIO"
    NRMATRICULA:   Mapped[int]      = mapped_column(INTEGER,      nullable=False, primary_key=True)
    NMFUNCIONARIO: Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    DSFUNCAO:      Mapped[str]      = mapped_column(VARCHAR(100), nullable=False)
    DTADMISSAO:    Mapped[datetime] = mapped_column(DATE,         nullable=False)
    PESSOA_IDPESSOA:     Mapped[int]      = mapped_column(INTEGER, ForeignKey(Pessoa.IDPESSOA), nullable=False)