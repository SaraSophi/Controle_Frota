from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from services.db import session
from sqlalchemy import text
from models.CtVinculo import CtVinculo
from models.Motorista import Motorista
from models.Funcionario import Funcionario
from models.Veiculo_model import Veiculo

class DesvincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtDesvinculo.ui', self)
        self.botaoSalvar.clicked.connect(self.desvincular_motorista)
        self.show()

    def desvincular_motorista(self):
        try:
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            nrMatricula  = self.matriculaMotorista.text()
            nrFrota      = self.nrFrota.text()

            # Localize o ID do vinculo com os atributos fornecidos e DTDESVINCULO nulo
            idVinculo = self.localizar_id_vinculo(nrFrota, nrMatricula)
            if idVinculo is None:
                raise ValueError("Vinculo não encontrado ou já desvinculado.")

            # Atualize o campo DTDESENGATE com a nova data
            vinculo = session.query(CtVinculo).get(idVinculo)
            vinculo.DTDESVINCULO = dtDesvinculo
            session.commit()

            QMessageBox.information(self, "Sucesso", "Data de desengate atualizada com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar data de desengate: {str(e)}")

    def localizar_id_vinculo(self, nrFrota, nrMatricula):
        # Obtenha os IDs do veículo e do motorista a partir das consultas
        id_veiculo = session.query(Veiculo.IDVEICULO).filter(Veiculo.NRFROTA == nrFrota).first()
        id_motorista = session.query(Motorista).join(Funcionario, Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()

        # Localize o ID do engate com os atributos fornecidos e DTDESVINCULO nulo
        id_vinculo = session.query(CtVinculo.ID).filter(
            CtVinculo.VEICULO_IDVEICULO == id_veiculo,
            CtVinculo.MOTORISTA_IDMOTORISTA == id_motorista,
            CtVinculo.DTDESVINCULO.is_(None)
        ).scalar()
        return id_vinculo


class VincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtVinculo.ui', self)
        self.criando_novo_vinculo()
        self.botaoTelaDesvinculo.clicked.connect(self.chamar_tela_desvinculo)
        self.show()
        self.desvincula_view = None

    def criando_novo_vinculo(self):
        self.botaoSalvar.clicked.connect(self.criando_vinculo_motorista)

    def criando_vinculo_motorista(self):
        try:
            dtVinculo    = self.dtVinculo.date().toPyDate()
            nrMatricula  = self.matriculaMotorista.text()
            nrFrota      = self.nrFrota.text()
            self.desvinculo_view = None

            id_motorista = VincularMotorista.procurar_motorista(nrMatricula)
            id_veiculo = VincularMotorista.procurar_frota(nrFrota)

            novo_vinculo = CtVinculo(DTVINCULO=dtVinculo, DTDESVINCULO=None,
                                     MOTORISTA_IDMOTORISTA=id_motorista, VEICULO_IDVEICULO=id_veiculo)
            session.add(novo_vinculo)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Motorista vinculado!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar vínculo: {str(e)}")

    def limpar_campos(self): #Função para limpar a tela ao terminar o cadastro

        self.dtVinculo.clear()
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

    def chamar_tela_desvinculo(self):
        if not self.desvincula_view:
            self.desvincula_view = DesvincularMotorista()
        self.desvincula_view.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VincularMotorista()
    app.exec()
