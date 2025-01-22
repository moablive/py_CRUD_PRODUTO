from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QMessageBox
from models.produto import Produto

class EditarProdutoDialog(QDialog):
    def __init__(self, parent, produto_id):
        """
        Janela de edição de produtos.
        O banco de dados será acessado via 'parent'.
        """
        super().__init__(parent)
        self.parent = parent
        self.produto_id = produto_id
        self.setWindowTitle("Editar Produto")
        self.setGeometry(300, 200, 400, 300)

        # Obter dados do produto pelo ID
        self.produto = self.parent.db.get_produto_by_id(self.produto_id)
        if not self.produto:
            QMessageBox.critical(self, "Erro", "Produto não encontrado!")
            return  # Evita fechar automaticamente

        # Criar objeto Produto com os dados obtidos
        produto_id, nome, descricao, preco, estoque = self.produto
        self.produto = Produto(nome, descricao, preco, estoque)

        # Layout do formulário
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Campos de entrada preenchidos com os valores atuais
        self.nome_input = QLineEdit(self.produto.nome)  
        self.descricao_input = QLineEdit(self.produto.descricao)  
        self.preco_input = QLineEdit(str(self.produto.preco))  
        self.estoque_input = QLineEdit(str(self.produto.estoque))  

        # Adicionando ao formulário
        form_layout.addRow(QLabel("Nome:"), self.nome_input)
        form_layout.addRow(QLabel("Descrição:"), self.descricao_input)
        form_layout.addRow(QLabel("Preço:"), self.preco_input)
        form_layout.addRow(QLabel("Estoque:"), self.estoque_input)

        layout.addLayout(form_layout)

        # Botão de salvar
        self.btn_salvar = QPushButton("Salvar Alterações")
        self.btn_salvar.clicked.connect(self.salvar_edicao)
        layout.addWidget(self.btn_salvar)

        self.setLayout(layout)

    def salvar_edicao(self):
        """Valida e salva as alterações no banco usando o modelo Produto."""
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

        # Criar um objeto Produto atualizado
        produto_editado = Produto(nome, descricao, preco, estoque)

        # Atualizar no banco via parent
        sucesso = self.parent.db.update_produto(self.produto_id, produto_editado)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso!")
            self.accept()  # Fecha a janela
        else:
            QMessageBox.critical(self, "Erro", "Erro ao atualizar o produto.")

def abrir_editar_produto(parent, produto_id):
    """Abre a janela de edição de produto."""
    dialog = EditarProdutoDialog(parent, produto_id)
    dialog.exec_()
