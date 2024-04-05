from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from services.db import session
from models.CtVinculo import CtVinculo
from models.Motorista import Motorista
from models.Funcionario import Funcionario
from models.Veiculo_model import Veiculo
from sqlalchemy import func


class DesvincularMotorista(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCtDesvinculo.ui', self)
        self.botaoSalvar.clicked.connect(self.desvincular_motorista)
        self.show()

    def desvincular_motorista(self):
        try:
            dtDesvinculo = self.dtDesvinculo.date().toPyDate()
            nrMatricula = self.matriculaMotorista.text()
            nrFrota = self.nrFrota.text()

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
        veiculo = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        motorista = session.query(Motorista).join(Funcionario,
                                                  Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()

        if veiculo is None or motorista is None:
            return None

        vinculos = session.query(CtVinculo).filter(
            CtVinculo.VEICULO_IDVEICULO == veiculo.IDVEICULO,
            CtVinculo.MOTORISTA_IDMOTORISTA == motorista.IDMOTORISTA,
            CtVinculo.DTDESVINCULO.is_(None)
        ).all()

        if len(vinculos) > 1:
            raise ValueError("Múltiplos vínculos ativos encontrados para o mesmo motorista e veículo.")
        elif len(vinculos) == 0:
            return None
        else:
            return vinculos[0].ID


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

    @staticmethod
    def procurar_motorista(nrMatricula):
        response = session.query(Motorista).join(Funcionario,
                                                 Funcionario.NRMATRICULA == Motorista.FUNCIONARIO_NRMATRICULA).filter(
            Motorista.FUNCIONARIO_NRMATRICULA == nrMatricula).first()
        id_motorista = response.IDMOTORISTA

        return id_motorista

    @staticmethod
    def procurar_frota(nrFrota):
        response = session.query(Veiculo).filter(Veiculo.NRFROTA == nrFrota).first()
        id_veiculo = response.IDVEICULO
        return id_veiculo

    def vinculado_or_no_frota(self, nrFrota):
        id_veiculo = VincularMotorista.procurar_frota(nrFrota)

        vinculos = session.query(CtVinculo.ID).filter(
            CtVinculo.VEICULO_IDVEICULO == id_veiculo,
            CtVinculo.DTDESVINCULO == None
        ).all()

        print("quantidade achada veiculos: ", vinculos)

        return len(vinculos)

    def vinculado_or_no_motorista(self, nrMatricula):
        id_motorista = int(VincularMotorista.procurar_motorista(nrMatricula))
        print(f"\n \n \n ID motorista {id_motorista}")
        print(f"ID's motorista banco {session.query(CtVinculo.MOTORISTA_IDMOTORISTA)}")

        vinculos = session.query(CtVinculo.ID).filter(
            CtVinculo.MOTORISTA_IDMOTORISTA == id_motorista,
            CtVinculo.DTDESVINCULO == None
        ).all()

        print("quantidade achada motorista: ", len(vinculos))
        print("Lista de vinculos", vinculos)

        return len(vinculos)

    def criando_vinculo_motorista(self):
        try:
            dtVinculo = self.dtVinculo.date().toPyDate()
            nrMatricula = self.matriculaMotorista.text()
            nrFrota = self.nrFrota.text()
            self.desvinculo_view = None

            id_motorista = VincularMotorista.procurar_motorista(nrMatricula)
            id_veiculo = VincularMotorista.procurar_frota(nrFrota)

            erros = []

            if self.vinculado_or_no_frota(nrFrota) > 0:
                erros.append("veiculo já vinculado")

            if self.vinculado_or_no_motorista(nrMatricula) > 0:
                erros.append("motorista já vinculado")

            if erros:
                QMessageBox.critical(self, "Erro", "\n".join(erros))
                return

            print(f"Data vinculo: {dtVinculo} \n IDMOTORISTA: {id_motorista} \n IDVEICULO: {id_veiculo}")
            novo_vinculo = CtVinculo(DTVINCULO=dtVinculo, DTDESVINCULO=None,
                                     MOTORISTA_IDMOTORISTA=id_motorista, VEICULO_IDVEICULO=id_veiculo)
            session.add(novo_vinculo)
            session.commit()

            QMessageBox.information(self, "Sucesso", "Motorista vinculado!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao criar vínculo: {str(e)}")

    def limpar_campos(self):  # Função para limpar a tela ao terminar o cadastro

        self.dtVinculo.clear()
        self.nrMatricula.clear()
        self.nrFrota.clear()

    # def verificar_data(self, dtVinculo):

    def chamar_tela_desvinculo(self):
        if not self.desvincula_view:
            self.desvincula_view = DesvincularMotorista()
        self.desvincula_view.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VincularMotorista()
    app.exec()
