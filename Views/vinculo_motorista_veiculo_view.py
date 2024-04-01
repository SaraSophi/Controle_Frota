from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from services.db import session
from sqlalchemy import text
from models.CtVinculo import CtVinculo
from models.Motorista import Motorista
from models.Funcionario import Funcionario
from models.Veiculo_model import Veiculo

class VincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtVinculo.ui', self)
        self.criando_novo_vinculo()
        self.show()

    def criando_novo_vinculo(self):
        self.botaoSalvar.clicked.connect(self.criando_vinculo_motorista)

    def criando_vinculo_motorista(self):
        try:
            dtVinculo    = self.dtVinculo.date().toPyDate()
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            nrMatricula  = self.matriculaMotorista.text()
            nrFrota      = self.nrFrota.text()

            id_motorista = VincularMotorista.procurar_motorista(nrMatricula)
            id_veiculo = VincularMotorista.procurar_frota(nrFrota)

            novo_vinculo = CtVinculo(DTVINCULO=dtVinculo, DTDESVINCULO=dtDesvinculo,
                                     MOTORISTA_IDMOTORISTA=id_motorista, VEICULO_IDVEICULO=id_veiculo)
            session.add(novo_vinculo)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Motorista vinculado!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar vínculo: {str(e)}")

    def limpar_campos(self): #Função para limpar a tela ao terminar o cadastro

        self.dtVinculo.clear()
        self.dtDesvinculo.clear()
        self.nrMatricula.clear()
        self.nrFrota.clear()

    def procurar_motorista(nrMatricula):
        response = session.query(Motorista).join(Funcionario,Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()
        id_motorista = response.IDMOTORISTA
        return id_motorista

    def procurar_frota(nrFrota):
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        id_veiculo = response.IDVEICULO
        return id_veiculo


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VincularMotorista()
    app.exec()
