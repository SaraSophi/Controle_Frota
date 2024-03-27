from PyQt5 import uic, QtWidgets
from cadastro_veiculo_view import CadastroVeiculoView
from cadastro_uf_view import  CadastroUf
from vinculo_motorista_veiculo_view import  VincularMotorista
class MenuInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaMenu.ui', self)
        self.show()
        self.botaoEntrarCadastroVeic.clicked.connect(self.ChamarCadastroVeiculo)
        self.botaoEntrarCadastroUf.clicked.connect(self.ChamarCadastroUf)
        self.botaoCtVinculo.clicked.connect(self.ChamarCtVinculoMotorista)
        self.cadastro_veiculo_view = None
        self.cadastro_uf_view = None
        self.vinculo_motorista_veiculo_view = None


    def ChamarCadastroVeiculo(self):
        if not self.cadastro_veiculo_view:
            self.cadastro_veiculo_view = CadastroVeiculoView()
        self.cadastro_veiculo_view.show()

    def ChamarCadastroUf(self):
        if not self.cadastro_uf_view:
            self.cadastro_uf_view = CadastroUf()
        self.cadastro_uf_view.show()

    def ChamarCtVinculoMotorista(self):
        if not self.vinculo_motorista_veiculo_view:
            self.vinculo_motorista_veiculo_view = VincularMotorista()
        self.vinculo_motorista_veiculo_view.show()



if __name__ == "__main__": #Inicando a tela
    app = QtWidgets.QApplication([])
    window = MenuInicial()
    app.exec()