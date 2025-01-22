import shutil
import os

def limpar_pycache():
    """Remove diretórios __pycache__ dentro do projeto."""
    cache_dirs = ["menu/__pycache__", 
                  "db/__pycache__"]  # Adicione mais diretórios conforme necessário

    for cache_dir in cache_dirs:
        full_path = os.path.join(os.path.dirname(__file__), "..", cache_dir)  # Ajustando o caminho
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            print(f"🗑️  Diretório {cache_dir} removido!")
