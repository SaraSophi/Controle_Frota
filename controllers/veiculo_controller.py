'''
import re
from datetime import datetime

class VeiculoController:
    @staticmethod
    def menu_veiculo():
        MenuView.clear()
        print("Menu de Produtos")
        print("1 - Cadastrar Produto")
        print("2 - Cadastrar Ingrediente")
        print("3 - Listar Produtos")
        print("4 - Listar Ingredientes")
        print("0 - Voltar")

        return MenuView.option()
    def __init__(self, idVeic, nrPlaca, dsModelo, tpTracao, nrRenavam, dtAquisicao, nrFrota, nrConjunto, nrChassi, tpCombustivel, anoVeic, dsMarca, qtEixo):        
        self.idVeic        = idVeic
        self.set_nrPlaca   (nrPlaca)
        self.dsModelo      = dsModelo
        self.tpTracao      = tpTracao
        self.set_nrRenavam (nrRenavam)
        self.dtAquisicao   = dtAquisicao
        self.nrFrota       = nrFrota
        self.nrConjunto    = nrConjunto
        self.set_nrChassi  (nrChassi)
        self.tpCombustivel = tpCombustivel
        self.set_anoVeic   (anoVeic)
        self.dsMarca       = dsMarca
        self.qtEixo        = qtEixo
   
 # Getters - recuperar o valor
    def get_idVeic(self):
        return self.idVeic

    def get_nrPlaca(self):
        return self._nrPlaca

    def get_dsModelo(self):
        return self.dsModelo

    def get_tpTracao(self):
        return self.tpTracao

    def get_nrRenavam(self):
        return self._nrRenavam

    def get_dtAquisicao(self):
        return self.dtAquisicao

    def get_nrFrota(self):
        return self.nrFrota

    def get_nrConjunto(self):
        return self.nrConjunto

    def get_nrChassi(self):
        return self._nrChassi

    def get_tpCombustivel(self):
        return self.tpCombustivel

    def get_anoVeic(self):
        return self._anoVeic

    def get_dsMarca(self):
        return self.dsMarca

    def get_qtEixo(self):
        return self.qtEixo

    # Setters - modificar o valor
    def set_idVeic(self, idVeic):
        self.idVeic = idVeic
    
    def set_nrPlaca(self, nrPlaca):
        if self.validar_placa(nrPlaca):
            self._nrPlaca = nrPlaca
        else:
            raise ValueError("Placa inválida.")

    def set_dsModelo(self, dsModelo):
        self.dsModelo = dsModelo

    def set_tpTracao(self, tpTracao):
        self.tpTracao = tpTracao

    def set_nrRenavam(self, nrRenavam):
        if self.valida_renavam(nrRenavam):
            self._nrRenavam = nrRenavam
        else:
            raise ValueError("Renavam inválido.")

    def set_dtAquisicao(self, dtAquisicao):
        self.dtAquisicao = dtAquisicao

    def set_nrFrota(self, nrFrota):
        self.nrFrota = nrFrota

    def set_nrConjunto(self, nrConjunto):
        self.nrConjunto = nrConjunto

    def set_nrChassi(self, nrChassi):
        if self.valida_chassi(nrChassi):
            self._nrChassi = nrChassi
        else:
            raise ValueError("Chassi inválido.")

    def set_tpCombustivel(self, tpCombustivel):
        self.tpCombustivel = tpCombustivel

    def set_anoVeic(self, anoVeic):
        if self.valida_ano(anoVeic):
            self._anoVeic = anoVeic
        else:
            raise ValueError("Ano do veículo inválido.")

    def set_dsMarca(self, dsMarca):
        self.dsMarca = dsMarca

    def set_qtEixo(self, qtEixo):
        self.qtEixo = qtEixo

    # Validações gerais dos atributos
    def validar_placa(self, nrPlaca):
        padraoTradicional = r'^[A-Za-z]{3}\d{4}$'
        padraoMercosul = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
        return re.match(padraoTradicional, nrPlaca) or re.match(padraoMercosul, nrPlaca)

    def valida_renavam(self, nrRenavam):
        renavam = str(nrRenavam).zfill(11)
        if len(renavam) == 9:
            renavam = "00" + renavam
        elif len(renavam) != 11:
            return False
        
        d = [int(x) for x in renavam]
        soma = sum(d[i]*int(peso) for i, peso in enumerate("3298765432"))
        resto = soma % 11
        dv = 11 - resto if resto > 1 else 0
        return dv == d[-1]

    def valida_chassi(self, nrChassi):
        padraoChassi = r'^[A-HJ-NPR-Z0-9]{17}$'
        return re.match(padraoChassi, nrChassi)

    def valida_ano(self, anoVeic):
        return anoVeic > 2000

    def valida_data(self, dtAquisicao):
        separadores = ['-', '/']
        for separador in separadores:
            if separador in dtAquisicao:
                try:
                    datetime.strptime(dtAquisicao, f'%d{separador}%m{separador}%Y')
                    return True
                except ValueError:
                    pass
        try:
            dtAquisicao = f"{dtAquisicao[:2]}/{dtAquisicao[2:4]}/{dtAquisicao[4:]}"
            datetime.strptime(dtAquisicao, '%d/%m/%Y')
            return True
        except ValueError:
            return False

        #def validaCampos(self):
        #Validação dos campos obrigatorios

    def validaQtdEixo(self):
        try:
            # Passa eixos para número inteiro
            self.qtEixo = int(self.qtEixo)
            # Verifica se a quantidade de eixos está dentro do intervalo aceitável (1 a 10, por exemplo)
            if self.qtEixo == '':
                print("A quantidade de eixo deve ser informada.")
                return ValueError
            else:   

                if 1 <= self.qtEixo <= 10:
                    return True
                else:
                    return False
        except ValueError:
                # Se não for possível converter para inteiro, retorna False
                return False

   # def validaFrota(self):
    #    if self.tracao = 1  se for automotor incrementar

# Valores
tipoVeic        = TipoVeic(1,'Truck','Pesado')
classificacao   = Classificacao(1,'Caminhão') 
clOperacao      = Operacao()
#clOperacao.adicionarOperacao("KKJnhkjkjhglkjh")
modelos         = ["FH500 - Volvo", "FH400 - Volvo"]
tpCombustivel   = ["1- Diesel S10", "2- Diesel S500"]
tpTracao        = ["Automotor", "Reboque", "SemiReboque"]



class ConsultaVeiculoController:


        @staticmethod
        def menu_consulta():
            MenuView.clear()
            print("Menu de Produtos")
            print("1 - Cadastrar Produto")
            print("2 - Cadastrar Ingrediente")
            print("3 - Listar Produtos")
            print("4 - Listar Ingredientes")
            print("0 - Voltar")

            return MenuView.option()

'''

def cadastrar_veiculo(nrFrota, nrConjunto, nrPlaca, nrRenavam, nrChassi, qtdEixo, anoVeic, dsModelo, dsMarca, tpTracao, tpCombustivel, tpClassificacao, tpCategoria, tpOperacao, dtAquisicao):
    veiculo = Veiculo(
        nrFrota=nrFrota,
        nrConjunto=nrConjunto,
        nrPlaca=nrPlaca,
        nrRenavam=nrRenavam,
        nrChassi=nrChassi,
        dsModelo=dsModelo,
        dsMarca=dsMarca,
        tpTracao=tpTracao,
        tpCombustivel=tpCombustivel,
        qtEixo=qtdEixo,
        anoVeic=anoVeic,
        dtAquisicao=dtAquisicao,
        tpClassificacao=tpClassificacao,
        tpOperacao=tpOperacao,
        tpCategoria=tpCategoria
    )
    session.add(veiculo)
    session.commit()

def funcao_principal():
    # Obter os dados do formulário
    nrFrota = telaCadastro.nrFrota.text()
    nrConjunto = telaCadastro.nrConjunto.text()
    nrPlaca = telaCadastro.nrPlaca.text()
    nrRenavam = telaCadastro.nrRenavam.text()
    nrChassi = telaCadastro.nrChassi.text()
    qtdEixo = telaCadastro.qtdEixo.text()
    anoVeic = telaCadastro.anoVeic.text()
    dsModelo = telaCadastro.dsModelo.currentText()
    dsMarca = telaCadastro.dsMarca.currentText()
    tpTracao = telaCadastro.tpTracao.currentText()
    tpCombustivel = telaCadastro.tpCombustivel.currentText()
    tpClassificacao = telaCadastro.tpClassificacao.currentText()
    tpCategoria = telaCadastro.tpCategoria.currentText()
    tpOperacao = telaCadastro.tpOperacao.currentText()
    dtAquisicao = telaCadastro.dtAquisicao.date()

    # Log dos dados do formulário
    logger.debug(f"Dados do formulário: {nrFrota}, {nrConjunto}, {nrPlaca}, {nrRenavam}, {nrChassi}, {qtdEixo}, {anoVeic}, {dsModelo}, {dsMarca}, {tpTracao}, {tpCombustivel}, {tpClassificacao}, {tpCategoria}, {tpOperacao}, {dtAquisicao}")

    # Chamar a função para cadastrar o veículo
    cadastrar_veiculo(nrFrota, nrConjunto, nrPlaca, nrRenavam, nrChassi, qtdEixo, anoVeic, dsModelo, dsMarca, tpTracao, tpCombustivel, tpClassificacao, tpCategoria, tpOperacao, dtAquisicao)