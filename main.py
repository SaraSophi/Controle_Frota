'''
from utils.create_db import create_db
from controllers.app_controller import AppController

if _name_ == "_main_":
    create_db()
    app = AppController()
    app.menu()

'''