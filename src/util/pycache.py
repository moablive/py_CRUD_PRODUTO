import shutil
import os

def limpar_pycache():
    """Remove todos os diretórios __pycache__ dentro do projeto, percorrendo recursivamente."""
    
    projeto_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Diretório raiz do projeto

    for root, dirs, files in os.walk(projeto_root):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"🗑️  Diretório {pycache_path} removido!")
            except Exception as e:
                print(f"⚠️  Erro ao remover {pycache_path}: {e}")

# Executar a função ao rodar o script
if __name__ == "__main__":
    limpar_pycache()