from PyQt5 import uic, QtWidgets
from cadastro_veiculo_view import CadastroVeiculoView

class MenuInicial(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaMenu.ui', self)
        self.show()
        self.botaoEntrarCadastroVeic.clicked.connect(self.ChamarCadastroVeiculo)
        self.cadastro_veiculo_view = None


    def ChamarCadastroVeiculo(self):
        if not self.cadastro_veiculo_view:
            self.cadastro_veiculo_view = CadastroVeiculoView()
        self.cadastro_veiculo_view.show()


if __name__ == "__main__": #Inicando a tela
    app = QtWidgets.QApplication([])
    window = MenuInicial()
    app.exec()