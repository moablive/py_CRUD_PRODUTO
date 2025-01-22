# python imports
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# Project
from menu.banco import actions_mariaDB
from db.mariadb import MariaDB
from util.pycache import limpar_pycache  # LIMPA pycache.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD DE PRODUTO")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("assets/appICO.ico")) 

        # Iniciar conexão com o banco
        self.db = MariaDB()

        # Criar a barra de menu
        menu_bar = self.menuBar()

        # Criar o menu "Banco"
        banco_menu = menu_bar.addMenu("Banco")
        
        # Adicionar ações ao menu "Gerenciador" usando a função importada
        actions_mariaDB(banco_menu, self)

# Inicializar o aplicativo
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
