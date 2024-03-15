import tkinter as tk
from tkinter import ttk

class TelaVeiculo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cadastro de Veículo")
        self.geometry("600x600")

        self.label_placa = tk.Label(self, text="Placa:")
        self.label_placa.pack()

        self.entry_placa = tk.Entry(self)
        self.entry_placa.pack()

        self.label_modelo = tk.Label(self, text="Modelo:")
        self.label_modelo.pack()

        self.combobox_modelo = ttk.Combobox(self, values=["FH500 - Volvo", "FH400 - Volvo"])
        self.combobox_modelo.pack()

        self.label_tp_tracao = tk.Label(self, text="Tipo de Tração:")
        self.label_tp_tracao.pack()

        self.combobox_tp_tracao = ttk.Combobox(self, values=["Automotor", "Reboque", "SemiReboque"])
        self.combobox_tp_tracao.pack()

        self.label_nr_renavam = tk.Label(self, text="Renavam:")
        self.label_nr_renavam.pack()

        self.entry_nr_renavam = tk.Entry(self)
        self.entry_nr_renavam.pack()

        self.label_dt_aquisicao = tk.Label(self, text="Data de Aquisição:")
        self.label_dt_aquisicao.pack()

        self.entry_dt_aquisicao = tk.Entry(self)
        self.entry_dt_aquisicao.pack()

        self.label_nr_frota = tk.Label(self, text="Número da Frota:")
        self.label_nr_frota.pack()

        self.entry_nr_frota = tk.Entry(self)
        self.entry_nr_frota.pack()

        self.label_nr_conjunto = tk.Label(self, text="Número do Conjunto:")
        self.label_nr_conjunto.pack()

        self.entry_nr_conjunto = tk.Entry(self)
        self.entry_nr_conjunto.pack()

        self.label_nr_chassi = tk.Label(self, text="Chassi:")
        self.label_nr_chassi.pack()

        self.entry_nr_chassi = tk.Entry(self)
        self.entry_nr_chassi.pack()

        self.label_tp_combustivel = tk.Label(self, text="Tipo de Combustível:")
        self.label_tp_combustivel.pack()

        self.combobox_tp_combustivel = ttk.Combobox(self, values=["1- Diesel S10", "2- Diesel S500"])
        self.combobox_tp_combustivel.pack()

        self.label_ano_veic = tk.Label(self, text="Ano do Veículo:")
        self.label_ano_veic.pack()

        self.entry_ano_veic = tk.Entry(self)
        self.entry_ano_veic.pack()

        self.label_ds_marca = tk.Label(self, text="Marca:")
        self.label_ds_marca.pack()

        self.combobox_ds_marca = ttk.Combobox(self, values=["Volvo", "Scania"])
        self.combobox_ds_marca.pack()

        self.label_qt_eixo = tk.Label(self, text="Quantidade de Eixos:")
        self.label_qt_eixo.pack()

        self.entry_qt_eixo = tk.Entry(self)
        self.entry_qt_eixo.pack()

        self.button_salvar = tk.Button(self, text="Cadastrar", command=self.salvar_veiculo)
        self.button_salvar.pack()

    def salvar_veiculo(self):
        nrPlaca = self.entry_placa.get()
        dsModelo = self.combobox_modelo.get()
        tpTracao = self.combobox_tp_tracao.get()
        nrRenavam = self.entry_nr_renavam.get()
        dtAquisicao = self.entry_dt_aquisicao.get()
        nrFrota = self.entry_nr_frota.get()
        nrConjunto = self.entry_nr_conjunto.get()
        nrChassi = self.entry_nr_chassi.get()
        tpCombustivel = self.combobox_tp_combustivel.get()
        anoVeic = self.entry_ano_veic.get()
        dsMarca = self.combobox_ds_marca.get()
        qtEixo = self.entry_qt_eixo.get()

        # Enviar os dados para o back-end
        # Implementação futura

if __name__ == "__main__":
    app = TelaVeiculo()
    app.mainloop()
