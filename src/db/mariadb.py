import pymysql
import sys

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