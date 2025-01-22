from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox

class DeletarProdutoDialog(QDialog):
    def __init__(self, parent):
        """
        Janela para exibir a lista de produtos e permitir exclusão.
        """
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Deletar Produto")
        self.setGeometry(200, 200, 700, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Criar a tabela
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # Define 5 colunas
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Preço", "Estoque"])

        # Preencher a tabela com os produtos do banco
        self.carregar_produtos()

        # Conectar evento de clique duplo para deletar o produto selecionado
        self.table.cellDoubleClicked.connect(self.produto_selecionado)

        # Adicionar a tabela ao layout
        layout.addWidget(self.table)
        self.setLayout(layout)

    def carregar_produtos(self):
        """Obtém todos os produtos do banco e preenche a tabela."""
        produtos = self.parent.db.select_all()  # Obtém os produtos via parent

        self.table.setRowCount(len(produtos))  # Define o número de linhas

        for row, produto in enumerate(produtos):
            id, nome, descricao, preco, estoque, _ = produto  # Ajuste conforme a estrutura da tabela

            # Preencher as células
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(row, 1, QTableWidgetItem(nome))
            self.table.setItem(row, 2, QTableWidgetItem(descricao))
            self.table.setItem(row, 3, QTableWidgetItem(f"R$ {preco:.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(str(estoque)))

    def produto_selecionado(self, row, column):
        """Obtém o ID do produto clicado e exibe um diálogo de confirmação antes de excluir."""
        produto_id = int(self.table.item(row, 0).text())  # Obtém o ID do produto

        # Confirmar exclusão
        confirmacao = QMessageBox.question(
            self,
            "Excluir Produto",
            f"Tem certeza que deseja excluir o produto ID {produto_id}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirmacao == QMessageBox.Yes:
            sucesso = self.parent.db.delete_produto(produto_id)
            if sucesso:
                QMessageBox.information(self, "Sucesso", "Produto excluído com sucesso!")
                self.carregar_produtos()  # Recarregar a tabela após exclusão
            else:
                QMessageBox.critical(self, "Erro", "Erro ao excluir o produto.")

def abrir_deletar_produto(parent):
    """Abre a tela de seleção de produto para exclusão."""
    dialog = DeletarProdutoDialog(parent)
    dialog.exec_()
