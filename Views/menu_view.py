import os


class MenuView:
    @staticmethod
    def clear():
        os.system('cls')
        print("\n\n")

    @staticmethod
    def option():
        valid = False
        while (not valid):
            try:
                option = int(input("\nDigite sua opção: "))
                valid = True
            except KeyboardInterrupt:
                option = 0
                valid = True
            except ValueError:
                option = None
                valid = True
            except Exception:
                valid = False

        return option

    @staticmethod
    def menu() -> int:
        MenuView.clear()
        print("MENU PRINCIPAL \n")
        print("1 - Cadastrar Veículo")
        print("2 - Consulta Veículo")
        print("3 - Vínculo e desvinculo de Motorista")
        print("4 - Engate e desengate de veículos")
        print("0 - Sair")

        return MenuView.option()
