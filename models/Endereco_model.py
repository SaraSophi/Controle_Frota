from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, VARCHAR, ForeignKey, Column
from models import Pessoa, Municipio

Base = declarative_base()
class Endereco_model(Base):
    _tablename_= "Endereco"
    idEndereco = Column(Integer, nullable=False, primary_key=True,autoincrement=True)
    dsLogradouro:        Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    nrCasa:              Mapped[int] = mapped_column(Integer, nullable=False)
    nmBairro:            Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    nrCep:               Mapped[int] = mapped_column(Integer(8), nullable=False)
    municipioCdMunicipio:Mapped[int] = mapped_column(Integer, ForeignKey(Municipio.cdMunicipio))
    pessoaIdPessoa:      Mapped[int] = mapped_column(Integer, ForeignKey(Pessoa.idPessoa))