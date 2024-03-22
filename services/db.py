from PyQt5 import uic, QtWidgets
from urllib.parse import quote
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, session
import cx_Oracle
import logging
from models import Veiculo_model
from datetime import date

lib_dir = "C:\oracle\instantclient_21_13"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Informando para o banco qual o meu usuário e senha, e o servidor em que o banco está
USER = 'system'
PASSWD = quote('ksl1708')
HOST = 'localhost'
PORT = 1521
SID = "xe"

sid = cx_Oracle.makedsn(HOST, PORT, sid=SID)
instance = f"oracle+cx_oracle://{USER}:{PASSWD}@{sid}"

engine = create_engine(url=instance, echo=True, max_identifier_length=30)
session = scoped_session(sessionmaker(bind=engine, autoflush=True, autocommit=False))



response = session.execute(text('SELECT * from veiculo'))
session.commit()
for row in response:
 print(row)

def funcao_principal():
    nrFrota = telaCadastro.nrFrota.text()
    nrConjunto = telaCadastro.nrConjunto.text()
    nrPlaca = telaCadastro.nrPlaca.text()
    nrRenavam = telaCadastro.nrRenavam.text()
    nrChassi = telaCadastro.nrChassi.text()
    qtdEixo = telaCadastro.qtdEixo.text()
    anoVeic = telaCadastro.anoVeic.text()
    dsModelo = telaCadastro.dsModelo.currentText()
    dsMarca = telaCadastro.dsMarca.currentText()
    tpTracao = telaCadastro.tpTracao.currentText()
    tpCombustivel = telaCadastro.tpCombustivel.currentText()
    tpClassificacao = telaCadastro.tpClassificacao.currentText()
    tpCategoria = telaCadastro.tpCategoria.currentText()
    tpOperacao = telaCadastro.tpOperacao.currentText()
    dtAquisicao = telaCadastro.dtAquisicao.date().toPyDate()  # Converte QDate para date
    print("cadastrado")
    logger.debug(f"Dados do formulário: {nrFrota}, {nrConjunto}, {nrPlaca}, {nrRenavam}, {nrChassi}, {qtdEixo}, {anoVeic}, {dsModelo}, {dsMarca}, {tpTracao}, {tpCombustivel}, {tpClassificacao}, {tpCategoria}, {tpOperacao}, {dtAquisicao}")

app = QtWidgets.QApplication([])
telaCadastro = uic.loadUi("telaCadastro.ui")
telaCadastro.botaoCadastrar.clicked.connect(funcao_principal)
def cadastrar_veiculo(nrFrota, nrConjunto, nrPlaca, nrRenavam, nrChassi, qtdEixo, anoVeic, dsModelo, dsMarca, tpTracao, tpCombustivel, tpClassificacao, tpCategoria, tpOperacao, dtAquisicao):
    veiculo = Veiculo_model(
        nrFrota=nrFrota,
        nrConjunto=nrConjunto,
        nrPlaca=nrPlaca,
        nrRenavam=nrRenavam,
        nrChassi=nrChassi,
        dsModelo=dsModelo,
        dsMarca=dsMarca,
        tpTracao=tpTracao,
        tpCombustivel=tpCombustivel,
        qtEixo=qtdEixo,
        anoVeic=anoVeic,
        dtAquisicao=dtAquisicao,
        tpClassificacao=tpClassificacao,
        tpOperacao=tpOperacao,
        tpCategoria=tpCategoria
    )



    cadastrar_veiculo(nrFrota, nrConjunto, nrPlaca, nrRenavam, nrChassi, qtdEixo, anoVeic, dsModelo, dsMarca, tpTracao, tpCombustivel, tpClassificacao, tpCategoria, tpOperacao, dtAquisicao)



telaCadastro.show()
app.exec()
session.add(cadastrar_veiculo)
session.commit()

response = session.execute(text('SELECT * from veiculo'))
session.commit()
for row in response:
 print(row)

