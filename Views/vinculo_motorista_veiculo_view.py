from PyQt5 import uic, QtWidgets
from services.db import session
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.exc import IntegrityError
from models.CtVinculo import CtVinculo

class VincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtVinculo.ui', self)
        self.show()

    def criando_vinculo_motorista(self):
        try:
            dtVinculo = self.dtVinculo.date().toPyDate()
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            idMotorista = self.idMotorista.text()
            idVeiculo = self.idVeiculo.text()
            nrFrota = self.nrFrota.text()

            novo_vinculo = CtVinculo (DTVINCULO = dtVinculo, DTDESVINCULO = dtDesvinculo, IDMOTORISTA = idMotorista, IDVEICULO = idVeiculo, NRFROTA = nrFrota)
            session.add(novo_vinculo)
            session.commit()


            QMessageBox.information(self, "Sucesso", "Motorista vinculado!")
            self.limpar_campos()
        except IntegrityError as e:
            session.rollback()
            QMessageBox.critical(self, "Erro", "Erro de integridade: pode haver um valor duplicado ou outro problema de restrição.")
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao realizar o vinculo do motorista: {e}")

    def limpar_campos(self): #Função para limpar a tela ao terminar o cadastro

        self.dtVinculo.clear()
        self.dtDesvinculo.clear()
        self.idMotorista.clear()
        self.idVeiculo.clear()
        self.nrFrota.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VincularMotorista()
    app.exec()
