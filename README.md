# 📦 CRUD de Produtos - PyQt5 + MariaDB

Um sistema de **CRUD** (Criar, Ler, Atualizar e Deletar) de produtos, desenvolvido com **Python + PyQt5** para a interface gráfica e **MariaDB** para o banco de dados.

---

## 🚀 Funcionalidades
✅ **Listar Produtos** - Exibe todos os produtos cadastrados.  
✅ **Adicionar Produto** - Permite cadastrar novos produtos.  
✅ **Editar Produto** - Seleciona um produto e permite edição de seus dados.  
✅ **Excluir Produto** - Exclui um produto após confirmação do usuário.  

---

## 📌 Tecnologias Utilizadas
- **Python 3.8+**
- **PyQt5** (Interface Gráfica)
- **MariaDB** (Banco de Dados)
- **PyMySQL** (Conexão com o Banco)

---

## ⚙️ Configuração do Banco de Dados (MariaDB)

### **1️⃣ Instalar MariaDB**
Caso não tenha o **MariaDB** instalado, siga as instruções abaixo:

#### **Windows**
Baixe o MariaDB em: [https://mariadb.org/download/](https://mariadb.org/download/)  
Após a instalação, inicie o serviço do MariaDB.

#### **Linux (Debian/Ubuntu)**
```sh
sudo apt update
sudo apt install mariadb-server mariadb-client
Após a instalação, inicie o serviço:

sh
Copy
Edit
sudo systemctl start mariadb
sudo systemctl enable mariadb
2️⃣ Criar o Banco de Dados
Abra o terminal do MariaDB e execute:

sql
Copy
Edit
CREATE DATABASE pyDeveloper;
3️⃣ Criar a Tabela produtos
Dentro do MariaDB, execute:

sql
Copy
Edit
USE pyDeveloper;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
4️⃣ Criar Usuário e Conceder Permissões
sql
Copy
Edit
CREATE USER 'moab'@'%' IDENTIFIED BY 'Guilherme@1998';
GRANT ALL PRIVILEGES ON pyDeveloper.* TO 'moab'@'%';
FLUSH PRIVILEGES;
🛠 Instalação e Configuração do Projeto
1️⃣ Clonar o Repositório
sh
Copy
Edit
git clone https://github.com/seu-repositorio/py-crud-produto.git
cd py-crud-produto
2️⃣ Criar um Ambiente Virtual (Opcional, Recomendado)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instalar Dependências
sh
Copy
Edit
pip install -r requirements.txt
▶️ Executando o Projeto
Após configurar o banco, execute o sistema com:

sh
Copy
Edit
python src/main.py