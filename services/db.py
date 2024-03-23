from PyQt5 import uic, QtWidgets
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
import cx_Oracle
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, VARCHAR, CHAR, Column, NUMERIC

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))

Base = declarative_base()
class Uf(Base):
    __tablename__ = "UF"
    cdUf     = Column('cdUf', NUMERIC, primary_key=True, autoincrement=True, nullable=False)
    nmUf     = Column('nmUf', VARCHAR(100), nullable=False)
    dsSigla  = Column('dsSigla', VARCHAR(2), nullable=False)


def testeUF(telaUF):
    nmUf = telaUF.nmUf.text()
    dsSigla = telaUF.dssigla.text()

    if not dsSigla:
        print("O campo dsSigla não pode estar vazio.")
        return

    nova_uf = Uf(cdUf=Uf.cdUf, nmUf=nmUf, dsSigla=dsSigla)
    session.add(nova_uf)
    session.commit()
    print("Registro inserido com sucesso.")

    print("Registro inserido com sucesso.")
    print("Conteúdo dos widgets:")
    print(f"nmUf: {nmUf}")
    print(f"dsSigla: {dsSigla}")

    try:
        session.commit()
        print("Registro inserido com sucesso.")
    except Exception as e:
        print("Erro ao inserir registro:", e)


app = QtWidgets.QApplication([])
telaUF = uic.loadUi("telaUF.ui")
telaUF.cadastrarUF.clicked.connect(lambda: testeUF(telaUF))
telaUF.show()
app.exec()

