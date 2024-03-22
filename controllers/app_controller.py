import sys
from Views.menu_view import MenuView
from controllers.veiculo_controller import VeiculoController
from controllers.veiculo_controller import ConsultaVeiculoController
from controllers.Vinculo_controller import VinculoController
from controllers.Engate_controller import EngateController
class AppController:
    def menu(self):
        exit = False
        while(not exit):
            option = MenuView.menu()
            match(option):
                case 1:
                    controller = VeiculoController()
                    controller.menu_veiculo()
                case 2:
                    controller = ConsultaVeiculoController()
                    controller.menu_consulta()
                case 3:
                    controller = VinculoController()
                    controller.menu_motorista()
                case 4:
                    controller = EngateController()
                    controller.menu_engate()
                case 0:
                    exit = True

