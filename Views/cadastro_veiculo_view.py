from PyQt5 import uic, QtWidgets
from services.db import session
from models.Veiculo_model import Veiculo
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.exc import IntegrityError
import re
from datetime import datetime

class CadastroVeiculoView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('telaCadastro.ui', self)
        self.criando_novo_veiculo()
        self.lista_veic = []
        self.show()

    def criando_novo_veiculo(self):
        self.botaoCadastrar.clicked.connect(self.registro_veiculo)

    def lista_veiculo(self):
        self.lista_veic = []

        response = session.query(Veiculo)
        for veic in response:
            self.lista_veic.append(veic)

        return self.lista_veic

    def lista_veiculo(self):
        # Recupera a lista de veículos do banco de dados e a armazena na lista_veic
        self.lista_veic = session.query(Veiculo).all()
        return self.lista_veic

    def registro_veiculo(self):
        try:
            nrFrota         = self.nrFrota.text()
            nrConjunto      = self.nrConjunto.text()
            nrPlaca         = self.nrPlaca.text()
            nrRenavam       = self.nrRenavam.text()
            dsModelo        = self.dsModelo.currentText()
            anoVeic         = int(self.anoVeic.text())
            dsMarca         = self.dsMarca.currentText()
            tpVeiculo       = self.tpVeiculo.currentText()
            tpCombustivel   = self.tpCombustivel.currentText()
            qtEixo          = int(self.qtdEixo.text())
            nrChassi        = self.nrChassi.text()
            tpTracao        = self.tpTracao.currentText()
            dtAquisicao     = self.dtAquisicao.date().toPyDate()

            campos_obrigatorios = [nrPlaca, nrRenavam, dsModelo, anoVeic, dsMarca, tpVeiculo, tpCombustivel, qtEixo,
                                   nrChassi, tpTracao, dtAquisicao]
            if any(campo == "" or campo is None for campo in campos_obrigatorios):
                QMessageBox.critical(self, "Erro", "Todos os campos devem ser preenchidos.")
                return

            # Validação Frota e Conjunto
            if nrFrota and nrConjunto:
                QMessageBox.critical(self, "Erro", "Apenas um dos campos 'Frota' ou 'Conjunto' deve ser preenchido.")
                return

            # Validação Frota não pode ser Reboque ou Semirreboque
            if tpTracao in ["Reboque", "SemiReboque"] and nrFrota:
                QMessageBox.critical(self, "Erro", "A frota não pode ser um Reboque/SemiReboque. Verifique se é um Conjunto ou Corrija a Tração do Veículo.")
                return
            # Validação Conjunto não pode ser Automotor
            if tpTracao in ["Automotor"] and nrConjunto:
                QMessageBox.critical(self, "Erro", "O Conjunto não pode ser um Automotor. Verifique se é uma Frota.")
                return

            #Validações para cadastro efetivo no banco
            erros = []
            if not self.validar_placa(nrPlaca):
                erros.append("Placa inválida!")
            if not self.validar_renavam(nrRenavam):
                erros.append("Renavam inválido!")
            if not self.valida_chassi(nrChassi):
                erros.append("Chassi inválido!")
            if not self.valida_ano(anoVeic, dtAquisicao):
                erros.append(
                    "O ano de fabricação do veículo deve ser no máximo 1 ano após a data de aquisição e posterior a 1980.")
            if erros:
                QMessageBox.critical(self, "Erro", "\n".join(erros))
                return

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
    def validar_placa(self, nrPlaca):  #Validação da placa para Mercosul ou modelo antigo;
        padraoTradicional = r'^[A-Za-z]{3}\d{4}$'
        padraoMercosul    = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
        return re.match(padraoTradicional, nrPlaca) or re.match(padraoMercosul, nrPlaca)
    def validar_renavam(self, nrRenavam):# Validação do renavam
        renavam         = str(nrRenavam).zfill(11)
        if len(renavam) == 9:
            renavam     = "00" + renavam
        elif len(renavam) != 11:
            return False

        d = [int(x) for x in renavam]
        soma = sum(d[i] * int(peso) for i, peso in enumerate("3298765432"))
        resto = soma % 11
        dv = 11 - resto if resto > 1 else 0
        return dv == d[-1]

    def valida_chassi(self, nrChassi): #Validação do chassi
        padraoChassi = r'^[A-HJ-NPR-Z0-9]{17}$'
        return re.match(padraoChassi, nrChassi)

    def valida_ano(self, anoVeic, dtAquisicao): #Verifica se o ano de fabricação de veiculo não é superior a 1 ano a mais do ano de aquisicao
        anoAquisicao = dtAquisicao.year
        return anoVeic <= (anoAquisicao + 1) and anoVeic > 1980

    def limpar_campos(self): #Função para limpar a tela ao terminar o cadastro
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
        self.qtdEixo.clear()
        self.nrChassi.clear()
        self.tpTracao.clear()

if __name__ == "__main__": #Inicando a tela
    app = QtWidgets.QApplication([])
    window = CadastroVeiculoView()
    app.exec()


