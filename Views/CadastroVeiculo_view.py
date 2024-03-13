from tkinter import ttk
from models import Veiculo_model
from services.db import session
from controllers.veiculo_controller import Veiculo

#Tela 1 -  Cadastro Veículo
class CadastroVeiculoApp:
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
app = CadastroVeiculoApp(root)
root.mainloop()
'''
class CadastroVeiculo_view():
    def create_cadastro_veiculo_widgets(self):
        #from views.menu_view import cad_veiculo
        
        self.frame_cadastro_veiculo = ttk.Frame(cad_veiculo)
        self.frame_cadastro_veiculo.pack(padx=0, pady=10)

        self.label_placa = ttk.Label(self.frame_cadastro_veiculo, text="Placa:")
        self.label_placa.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.placa_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.placa_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_chassi = ttk.Label(self.frame_cadastro_veiculo, text="Chassi:")
        self.label_chassi.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.chassi_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.chassi_entry.grid(row=1, column=1, padx=5, pady=5)

        self.label_modelo = ttk.Label(self.frame_cadastro_veiculo, text="Modelo:")
        self.label_modelo.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.modelo_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.modelo_entry.grid(row=2, column=1, padx=5, pady=5)

        self.label_ano_modelo = ttk.Label(self.frame_cadastro_veiculo, text="Ano Modelo:")
        self.label_ano_modelo.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.ano_modelo_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.ano_modelo_entry.grid(row=3, column=1, padx=5, pady=5)

        self.label_hodometro = ttk.Label(self.frame_cadastro_veiculo, text="Hodômetro:")
        self.label_hodometro.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.hodometro_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.hodometro_entry.grid(row=4, column=1, padx=5, pady=5)

        self.label_status_manutencao = ttk.Label(self.frame_cadastro_veiculo, text="Status de Manutenção:")
        self.label_status_manutencao.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.status_manutencao_listbox = ttk.Combobox(self.frame_cadastro_veiculo, values = ["1 - Vencida", "2 - Em dia"])
        self.status_manutencao_listbox.grid(row=5, column=1, padx=5, pady=5)

        self.label_id_categoria = ttk.Label(self.frame_cadastro_veiculo, text="ID da Categoria:")
        self.label_id_categoria.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.id_categoria_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.id_categoria_entry.grid(row=6, column=1, padx=5, pady=5)

        self.label_id_frota = ttk.Label(self.frame_cadastro_veiculo, text="ID da Frota:")
        self.label_id_frota.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.id_frota_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.id_frota_entry.grid(row=8, column=1, padx=5, pady=5)

        self.btn_cadastrar = ttk.Button(self.frame_cadastro_veiculo, text="Cadastrar veículo", 
                                        command=self.registro_veiculo)
        self.btn_cadastrar.grid(row=10, columnspan=2, pady=10)

    def limpar_campos(self):
        self.placa_entry.delete(0, 'end')
        self.chassi_entry.delete(0, 'end')
        self.modelo_entry.delete(0, 'end')
        self.ano_modelo_entry.delete(0, 'end')
        self.hodometro_entry.delete(0, 'end')
        self.status_manutencao_listbox.set('')
        self.id_categoria_entry.delete(0, 'end')
        self.id_frota_entry.delete(0, 'end')
        self.placa          = placa
        self.anoVeic        = anoVeic
        self.renavam        = renavam
        self.chassi         = chassi
        self.tipoVeic       = tipoVeic
        self.classificacao  = classificacao
        self.modelo         = modelo
        self.operacao       = operacao
        self.combustivel    = combustivel
        self.dtAquisicao    = dtAquisicao
        self.cor            = cor
        self.tracao         = tracao
        self.qtEixo         = qtEixo
        self.frota          = frota

    def veiculo_info(self):
        placa: str = str(self.placa_entry.get())
        chassi: str = str(self.chassi_entry.get())
        modelo: str = str(self.modelo_entry.get())
        ano_modelo: int = int(self.ano_modelo_entry.get())
        hodometro: int = int(self.hodometro_entry.get())
        status_manutencao: str = str(self.status_manutencao_listbox.get())
        frota_id: int = int(self.id_frota_entry.get())
        categoria_veiculo_id: int = int(self.id_categoria_entry.get())
        
        return placa, chassi, modelo, ano_modelo, hodometro, status_manutencao, categoria_veiculo_id, frota_id
    
    def registro_veiculo(self):
        try:
            veiculo_veiculo = self.veiculo_info()
            placa, chassi, modelo, ano_modelo, hodometro, status_manutencao, categoria_veiculo_id, frota_id = veiculo_veiculo
            
            if status_manutencao == "1 - Vencida":
                status_manutencao = "1"
            else:
                status_manutencao = "2"

            veiculo = Veiculo(placa=placa, chassi=chassi, modelo=modelo, ano_modelo=ano_modelo, hodometro=hodometro, 
                              status_manutencao=status_manutencao, categoria_veiculo_id=categoria_veiculo_id, frota_id=frota_id)
             
            session.add(veiculo)
            session.commit()

            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o veículo: {e}")

            '''