import pymysql
import sys

# Models
from models.produto import Produto

class MariaDB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="moab-server.ddns.me",
                user="moab",
                password="Guilherme@1998",
                database="pyDeveloper",
                port=3306
            )
            self.cursor = self.conn.cursor()
            print("✅ Conexão com o banco MariaDB estabelecida com sucesso!")
        except pymysql.MySQLError as e:
            print(f"❌ Erro ao conectar ao MariaDB: {e}")
            sys.exit(1)

    def close_conection(self):
        """ Fecha a conexão com o banco de dados """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("🔌 Conexão com o MariaDB encerrada.")

    def select_all(self):
        """ Busca todos os registros da tabela 'produtos' """
        query = "SELECT * FROM produtos"
        try:
            self.cursor.execute(query)
            produtos = self.cursor.fetchall()

            if not produtos:
                print("⚠️ Nenhum produto encontrado.")
                return []

            print("📦 Lista de Produtos:")
            for produto in produtos:
                print(produto)

            return produtos

        except pymysql.MySQLError as e:
            print(f"❌ Erro ao buscar produtos: {e}")
            return []
        
    def get_produto_by_id(self, produto_id):
        """Obtém um produto pelo ID."""
        query = "SELECT id, nome, descricao, preco, estoque FROM produtos WHERE id = %s"
        try:
            self.cursor.execute(query, (produto_id,))
            produto = self.cursor.fetchone()
            return produto  # Retorna uma tupla ex: (1, "Produto A", "Descrição", 99.99, 10)
        except pymysql.MySQLError as e:
            print(f"❌ Erro ao buscar produto por ID: {e}")
            return None
        
    def add_produto(self, produto: Produto):
        """ Insere um novo produto na tabela 'produtos' """
        query = """
        INSERT INTO produtos (nome, descricao, preco, estoque)
        VALUES (%s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, (produto.nome, produto.descricao, produto.preco, produto.estoque))
            self.conn.commit()  # Salva as alterações no banco
            print(f"✅ Produto '{produto.nome}' cadastrado com sucesso!")
            return True
        except pymysql.MySQLError as e:
            print(f"❌ Erro ao cadastrar produto: {e}")
            return False
    
    def update_produto(self, produto_id, produto: Produto):
        """
        Atualiza um produto existente no banco de dados.
        
        :param produto_id: ID do produto que será atualizado.
        :param produto: Objeto Produto com os novos dados.
        :return: True se atualizado com sucesso, False caso contrário.
        """
        query = """
        UPDATE produtos
        SET nome = %s, descricao = %s, preco = %s, estoque = %s
        WHERE id = %s
        """
        try:
            self.cursor.execute(query, (produto.nome, produto.descricao, produto.preco, produto.estoque, produto_id))
            self.conn.commit()  # Salvar alterações no banco
            print(f"✅ Produto ID {produto_id} atualizado com sucesso!")
            return True
        except pymysql.MySQLError as e:
            print(f"❌ Erro ao atualizar produto: {e}")
            return False
    
    def delete_produto(self, produto_id):
        """Remove um produto pelo ID."""
        query = "DELETE FROM produtos WHERE id = %s"
        try:
            self.cursor.execute(query, (produto_id,))
            self.conn.commit()  # Confirma a remoção no banco
            print(f"✅ Produto ID {produto_id} excluído com sucesso!")
            return True
        except pymysql.MySQLError as e:
            print(f"❌ Erro ao excluir produto: {e}")
            return False