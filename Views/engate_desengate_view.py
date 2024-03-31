from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from services.db import session
from models.Veiculo_model import Veiculo
from models.CtEngate import CtEngate

class EngateDesengateVeiculo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtEngate.ui', self)
        self.criando_novo_engate()
        self.show()

    def criando_novo_engate(self):
        self.botaoSalvar.clicked.connect(self.criando_engate_desengate)

    def criando_engate_desengate(self):
        try:
            dtEngate = self.dtEngate.date().toPyDate()
            dtDesengate = self.dtDesengate.date().toPyDate()
            nrFrota = self.nrFrota.text()
            nrConjunto = self.nrConjunto.text()

            id_frota,cd_frota = EngateDesengateVeiculo.frota_existe(nrFrota)
            cd_conjunto = EngateDesengateVeiculo.conjunto_existe(nrConjunto)

            novo_engate = CtEngate(DTENGATE=dtEngate, DTDESENGATE=dtDesengate, NRFROTA=cd_frota, NRCONJUNTO=cd_conjunto, VEICULO_IDVEICULO = id_frota)
            session.add(novo_engate)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Veículo engatado/desengatado!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar vínculo: {str(e)}")

    @staticmethod
    def frota_existe(nrFrota):
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        id_frota = response.IDVEICULO
        cd_frota = response.NRFROTA
        return id_frota, cd_frota

    @staticmethod
    def conjunto_existe(nrConjunto):
        response = session.query(Veiculo).filter(Veiculo.NRCONJUNTO == nrConjunto).first()
        cd_conjunto = response.NRCONJUNTO
        return cd_conjunto




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = EngateDesengateVeiculo()
    app.exec()
