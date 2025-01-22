# python imports
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon

# Banco MariaDB
from db.mariadb import MariaDB

# Limpeza do __pycache__
from util.pycache import limpar_pycache  

# Actions
from actions.obterTodosOsProdutos import abrir_tela_produtos # GET
from actions.cadastrarProduto import abrir_cadastro_produto  # POST
from actions.selecionarProduto import abrir_selecionar_produto # PUT
from actions.deletarProduto import abrir_deletar_produto # DELETE

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

        # Criar o menu Produto
        menu_produto = menu_bar.addMenu("Gerenciamento de Produto") 

        # Criar ação "Obter Produtos"
        obter_action = QAction("Obter Produtos", self)
        obter_action.triggered.connect(lambda: abrir_tela_produtos(self)) 
        menu_produto.addAction(obter_action)
        
        # Criar ação "Cadastrar Produto"
        cadastrar_action = QAction("Cadastrar Produto", self)
        cadastrar_action.triggered.connect(lambda: abrir_cadastro_produto(self))  
        menu_produto.addAction(cadastrar_action)

        # Criar ação "Editar Produto"
        editar_action = QAction("Editar Produto", self)
        editar_action.triggered.connect(lambda: abrir_selecionar_produto(self))
        menu_produto.addAction(editar_action)
        
        # Criar ação "Excluir Produto"
        excluir_action = QAction("Excluir Produto", self)
        excluir_action.triggered.connect(lambda: abrir_deletar_produto(self))  # Abre a tela de seleção
        menu_produto.addAction(excluir_action)
if __name__ == "__main__":
    # Executar a limpeza de __pycache__
    limpar_pycache()

# Inicializar o aplicativo
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
