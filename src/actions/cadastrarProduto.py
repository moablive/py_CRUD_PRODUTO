from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QMenu

# Model
from models.produto import Produto 

class CadastroProdutoDialog(QDialog):
    def __init__(self, parent=None):
        """
        Janela de cadastro de produtos.
        O banco de dados será acessado via 'parent', sem instanciação direta.
        """
        super().__init__(parent)
        self.parent = parent  
        self.setWindowTitle("Cadastrar Produto")
        self.setGeometry(300, 200, 400, 300)

        # Layout do formulário
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Campos de entrada
        self.nome_input = QLineEdit()
        self.descricao_input = QLineEdit()
        self.preco_input = QLineEdit()
        self.estoque_input = QLineEdit()

        # Adicionando ao formulário
        form_layout.addRow(QLabel("Nome:"), self.nome_input)
        form_layout.addRow(QLabel("Descrição:"), self.descricao_input)
        form_layout.addRow(QLabel("Preço:"), self.preco_input)
        form_layout.addRow(QLabel("Estoque:"), self.estoque_input)

        layout.addLayout(form_layout)

        # Botão de salvar
        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.clicked.connect(self.salvar_produto)
        layout.addWidget(self.btn_salvar)

        self.setLayout(layout)

    def salvar_produto(self):
        """Valida os dados e registra o produto no banco usando o modelo Produto via parent."""
        nome = self.nome_input.text().strip()
        descricao = self.descricao_input.text().strip()
        preco = self.preco_input.text().strip()
        estoque = self.estoque_input.text().strip()

        # Validação dos campos obrigatórios
        if not nome or not preco or not estoque:
            QMessageBox.warning(self, "Erro", "Nome, Preço e Estoque são obrigatórios!")
            return

        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Preço deve ser um número decimal e Estoque deve ser um número inteiro.")
            return

        # Criar um objeto Produto
        produto = Produto(nome, descricao, preco, estoque)

        # Inserir no banco via parent (sem instanciar diretamente o banco)
        sucesso = self.parent.db.add_produto(produto)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Produto cadastrado com sucesso!")
            self.accept()  # Fecha a janela
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar produto.")

def abrir_cadastro_produto(parent):
    """Função para abrir a janela de cadastro de produto."""
    dialog = CadastroProdutoDialog(parent)
    dialog.exec_()  # Exibe a janela modal
