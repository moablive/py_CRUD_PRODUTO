from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from models.produto import Produto

class ProdutosGrid(QDialog):
    def __init__(self, parent=None):
        """
        Janela para exibir a lista de produtos em um QTableWidget.
        :param parent: A janela principal (QMainWindow) que contém a instância do banco.
        """
        super().__init__(parent)
        self.parent = parent  
        self.setWindowTitle("Lista de Produtos")
        self.setGeometry(200, 200, 700, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Criar a tabela
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # Definir número de colunas
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Preço", "Estoque"])

        # Preencher a tabela com os dados do banco
        self.carregar_dados()

        # Adicionar a tabela ao layout
        layout.addWidget(self.table)
        self.setLayout(layout)

    def carregar_dados(self):
        """Obtém os produtos do banco e preenche a tabela."""
        produtos_brutos = self.parent.db.select_all()  # Obtém os produtos via parent

        self.table.setRowCount(len(produtos_brutos))  # Define o número de linhas

        for row, produto in enumerate(produtos_brutos):
            id, nome, descricao, preco, estoque, _ = produto  # Ajuste conforme a estrutura da tabela
            obj_produto = Produto(nome, descricao, preco, estoque)

            # Inserir os dados na tabela
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(obj_produto.nome))
            self.table.setItem(row, 2, QTableWidgetItem(obj_produto.descricao))
            self.table.setItem(row, 3, QTableWidgetItem(f"R$ {obj_produto.preco:.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(str(obj_produto.estoque)))

def abrir_tela_produtos(parent):
    """Abre a tela de produtos como um grid."""
    dialog = ProdutosGrid(parent)
    dialog.exec_()
