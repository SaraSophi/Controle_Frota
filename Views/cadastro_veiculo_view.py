from PyQt5 import uic, QtWidgets
from services.db import session
from models.Veiculo_model import Veiculo
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.exc import IntegrityError
from datetime import datetime

class CadastroVeiculoView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCadastro.ui', self)
        self.criando_novo_veiculo()
        self.show()

    def criando_novo_veiculo(self):
        self.botaoCadastrar.clicked.connect(self.registro_veiculo)

    def lista_veiculo(self):
        self.lista_veic = []

        response = session.query(Veiculo)
        for veic in response:
            self.lista_veic.append(veic)

        return self.lista_veic

    def registro_veiculo(self):
        try:

            nrFrota         = self.nrFrota.text()
            nrConjunto      = self.nrConjunto.text()
            nrPlaca         = self.nrPlaca.text()
            nrRenavam       = self.nrRenavam.text()
            dsModelo        = self.dsModelo.currentText()
            anoVeic         = int(self.anoVeic.text())  # Convertido para inteiro
            dsMarca         = self.dsMarca.currentText()
            tpVeiculo       = self.tpVeiculo.currentText()
            tpCombustivel   = self.tpCombustivel.currentText()
            qtEixo          = self.qtdEixo.text()  # Convertido para inteiro
            nrChassi        = self.nrChassi.text()
            tpTracao        = self.tpTracao.currentText()
            dtAquisicao     = self.dtAquisicao.date().toPyDate()  # Mantido como objeto datetime

            #veiculo_idVeiculo = idVeic   VEICULO_IDVEICULO=veiculo_idVeiculo
            novo_veiculo = Veiculo(NRPLACA=nrPlaca, DSMODELO=dsModelo, TPTRACAO=tpTracao,
                                   NRRENAVAM=nrRenavam, DTAQUISICAO=dtAquisicao, NRFROTA=nrFrota,
                                   NRCONJUNTO=nrConjunto, NRCHASSI=nrChassi, TPCOMBUSTIVEL=tpCombustivel,
                                   ANOVEIC=anoVeic, DSMARCA=dsMarca, QTEIXO=qtEixo,
                                   TPVEICULO=tpVeiculo)

            session.add(novo_veiculo)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Veículo Cadastrado!")
            self.limpar_campos()
        except IntegrityError as e:
            session.rollback()
            QMessageBox.critical(self, "Erro", "Erro de integridade: pode haver um valor duplicado ou outro problema de restrição.")
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self,"Erro", f"Ocorreu um erro ao realizar o cadastro: {e}")

    def limpar_campos(self):

        self.idVeic.clear()
        self.nrFrota.clear()
        self.nrConjunto.clear()
        self.nrPlaca.clear()
        self.nrRenavam.clear()
        self.dsModelo.clear()
        self.anoVeic.clear()
        self.dsMarca.clear()
        self.tpVeiculo.clear()
        self.tpCombustivel.clear()
        self.dtAquisicao.clear()
        self.qtEixo.clear()
        self.nrChassi.clear()
        self.tpTracao.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = CadastroVeiculoView()

    app.exec()
