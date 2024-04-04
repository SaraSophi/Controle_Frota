from PyQt5 import uic, QtWidgets
from cadastro_veiculo_view import CadastroVeiculoView
from vinculo_motorista_veiculo_view import VincularMotorista
from engate_view import EngateDesengateVeiculo
class MenuInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaMenu.ui', self)
        self.show()
        self.botaoEntrarCadastroVeic.clicked.connect(self.ChamarCadastroVeiculo)
        self.botaoCtVinculo.clicked.connect(self.ChamarCtVinculoMotorista)
        self.botaoEngateDesengate.clicked.connect(self.ChamarEngateDesengate)
        self.cadastro_veiculo_view = None
        self.vinculo_motorista_veiculo_view = None
        self.engate_desengate_view = None

    def ChamarCadastroVeiculo(self):
        if not self.cadastro_veiculo_view:
            self.cadastro_veiculo_view = CadastroVeiculoView()
        self.cadastro_veiculo_view.show()
    def ChamarCtVinculoMotorista(self):
        if not self.vinculo_motorista_veiculo_view:
            self.vinculo_motorista_veiculo_view = VincularMotorista()
        self.vinculo_motorista_veiculo_view.show()

    def ChamarEngateDesengate(self):
        if not self.engate_desengate_view:
            self.engate_desengate_view = EngateDesengateVeiculo()
        self.engate_desengate_view.show()



if __name__ == "__main__": #Inicando a tela
    app = QtWidgets.QApplication([])
    window = MenuInicial()
    app.exec()