import re
from datetime import datetime
from Views.menu_view import MenuView

class VinculoController:

    @staticmethod
    def menu_motorista():
        MenuView.clear()
        print("Menu de Produtos")
        print("1 - Cadastrar Produto")
        print("2 - Cadastrar Ingrediente")
        print("3 - Listar Produtos")
        print("4 - Listar Ingredientes")
        print("0 - Voltar")

        return MenuView.option()