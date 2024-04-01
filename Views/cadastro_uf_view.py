from PyQt5 import uic, QtWidgets
from services.db import session
from models.Uf import Uf
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.exc import IntegrityError
import re
class CadastroUf(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCadastroUf.ui', self)
        self.criando_novo_uf()
        self.show()

    def criando_novo_uf(self):
            self.botaoCadastrarUf.clicked.connect(self.registro_uf)
    def lista_uf(self):
        self.lista_uf = []

        response = session.query(Uf)
        for listUf in response:
            self.lista_uf.append(listUf)

        return self.lista_uf
    def registro_uf(self):
        try:
            nmUf = self.nmUf.text()
            dsSigla = self.dsSigla.text()


            novo_uf = Uf (NMUF = nmUf, DSSIGLA = dsSigla)
            session.add(novo_uf)
            session.commit()

            QMessageBox.information(self, "Sucesso", "UF Cadastrado!")
            self.limpar_campos()
        except IntegrityError as e:
            session.rollback()
            QMessageBox.critical(self, "Erro", "Erro de integridade: pode haver um valor duplicado ou outro problema de restrição.")
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self,"Erro", f"Ocorreu um erro ao realizar o cadastro: {e}")


    def limpar_campos(self): #Função para limpar a tela ao terminar o cadastro

        self.nmUf.clear()
        self.dsSigla.clear()

if __name__ == "__main__": #Inicando a tela
    app = QtWidgets.QApplication([])
    window = CadastroUf()

    app.exec()