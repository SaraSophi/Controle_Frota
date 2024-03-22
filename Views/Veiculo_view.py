from tkinter import ttk
from models import Veiculo_model
from services.db import session
from controllers.veiculo_controller import VeiculoController

#Tela 1 -  Cadastro Veículo
class Veiculo_view():


    def cadastro_veiculo_widgets(self):
        from Views.menu_view import MenuView

        self.frame_cadastro_veiculo = ttk.Frame(cad_veiculo)
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Veículo")

        # Label e Entry para cada atributo do veículo
        ttk.Label(root, text="ID do Veículo:").grid(row=0, column=0, sticky=tk.W)
        self.idVeic_entry = ttk.Entry(root)
        self.idVeic_entry.grid(row=0, column=1)

        ttk.Label(root, text="Número da Placa:").grid(row=1, column=0, sticky=tk.W)
        self.nrPlaca_entry = ttk.Entry(root)
        self.nrPlaca_entry.grid(row=1, column=1)

        ttk.Label(root, text="Modelo do Veículo:").grid(row=2, column=0, sticky=tk.W)
        self.modelo_var = tk.StringVar()
        self.modelo_dropdown = ttk.Combobox(root, textvariable=self.modelo_var)
        self.modelo_dropdown.grid(row=2, column=1)

        ttk.Label(root, text="Tipo de Tração:").grid(row=3, column=0, sticky=tk.W)
        self.tpTracao_entry = ttk.Entry(root)
        self.tpTracao_entry.grid(row=3, column=1)

        ttk.Label(root, text="Número do Renavam:").grid(row=4, column=0, sticky=tk.W)
        self.nrRenavam_entry = ttk.Entry(root)
        self.nrRenavam_entry.grid(row=4, column=1)

        ttk.Label(root, text="Data de Aquisição:").grid(row=5, column=0, sticky=tk.W)
        self.dtAquisicao_entry = ttk.Entry(root)
        self.dtAquisicao_entry.grid(row=5, column=1)

        ttk.Label(root, text="Número da Frota:").grid(row=6, column=0, sticky=tk.W)
        self.nrFrota_entry = ttk.Entry(root)
        self.nrFrota_entry.grid(row=6, column=1)

        ttk.Label(root, text="Número do Conjunto:").grid(row=7, column=0, sticky=tk.W)
        self.nrConjunto_entry = ttk.Entry(root)
        self.nrConjunto_entry.grid(row=7, column=1)

        ttk.Label(root, text="Número do Chassi:").grid(row=8, column=0, sticky=tk.W)
        self.nrChassi_entry = ttk.Entry(root)
        self.nrChassi_entry.grid(row=8, column=1)

        ttk.Label(root, text="Tipo de Combustível:").grid(row=9, column=0, sticky=tk.W)
        self.tpCombustivel_entry = ttk.Entry(root)
        self.tpCombustivel_entry.grid(row=9, column=1)

        ttk.Label(root, text="Ano do Veículo:").grid(row=10, column=0, sticky=tk.W)
        self.anoVeic_entry = ttk.Entry(root)
        self.anoVeic_entry.grid(row=10, column=1)

        ttk.Label(root, text="Marca do Veículo:").grid(row=11, column=0, sticky=tk.W)
        self.dsMarca_entry = ttk.Entry(root)
        self.dsMarca_entry.grid(row=11, column=1)

        ttk.Label(root, text="Quantidade de Eixos:").grid(row=12, column=0, sticky=tk.W)
        self.qtEixo_entry = ttk.Entry(root)
        self.qtEixo_entry.grid(row=12, column=1)

        # Botão para cadastrar veículo
        ttk.Button(root, text="Cadastrar Veículo", command=self.cadastrar_veiculo).grid(row=13, columnspan=2)

    def cadastrar_veiculo(self):
        try:
            # Coletando os dados do formulário
            idVeic = self.idVeic_entry.get()
            nrPlaca = self.nrPlaca_entry.get()
            modelo = self.modelo_var.get()
            tpTracao = self.tpTracao_entry.get()
            nrRenavam = self.nrRenavam_entry.get()
            dtAquisicao = self.dtAquisicao_entry.get()
            nrFrota = self.nrFrota_entry.get()
            nrConjunto = self.nrConjunto_entry.get()
            nrChassi = self.nrChassi_entry.get()
            tpCombustivel = self.tpCombustivel_entry.get()
            anoVeic = int(self.anoVeic_entry.get())
            dsMarca = self.dsMarca_entry.get()
            qtEixo = int(self.qtEixo_entry.get())

            # Criando o objeto Veiculo
            veiculo = Veiculo(idVeic, nrPlaca, modelo, tpTracao, nrRenavam, dtAquisicao, nrFrota, nrConjunto, nrChassi, tpCombustivel, anoVeic, dsMarca, qtEixo)
            
            # Exemplo de como você pode usar o veículo
            print("Veículo cadastrado com sucesso!")
            print("Modelo:", veiculo.get_dsModelo())
            print("Placa:", veiculo.get_nrPlaca())
            # Etc...

        except ValueError as e:
            # Tratando possíveis erros de validação
            tk.messagebox.showerror("Erro", str(e))

root = tk.Tk()
app = CadastroVeiculo(root)
root.mainloop()
