import tkinter as tk
from tkinter import ttk

class VeiculoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Veículos")

        # Lista de modelos disponíveis
        self.MODELOS_DISPONIVEIS = [
            "FH500 - Volvo",
            "FH400 - Volvo",
            "Outro Modelo"
        ]

        # Label e Dropdown para selecionar o modelo do veículo
        ttk.Label(root, text="Modelo do Veículo:").pack()
        self.modelo_var = tk.StringVar()
        self.modelo_dropdown = ttk.Combobox(root, textvariable=self.modelo_var, values=self.MODELOS_DISPONIVEIS)
        self.modelo_dropdown.pack()

        # Botão para cadastrar veículo
        ttk.Button(root, text="Cadastrar Veículo", command=self.cadastrar_veiculo).pack()

    def cadastrar_veiculo(self):
        modelo_selecionado = self.modelo_var.get()
        # Aqui você pode fazer o que quiser com o modelo selecionado, como criar um objeto Veiculo, por exemplo
        print("Veículo cadastrado com modelo:", modelo_selecionado)

root = tk.Tk()
app = VeiculoApp(root)
root.mainloop()
