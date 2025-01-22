from PyQt5.QtWidgets import QAction, QMessageBox

def actions_mariaDB(menu, parent):
    """
    Função para adicionar ações ao menu "Gerenciador".
    :param menu: O menu "Gerenciador" (QMenu)
    :param parent: A janela principal (QMainWindow) onde os métodos são chamados
    """

    # Botão "SELECT ALL" - Para buscar todos os produtos
    selectionALL = QAction("SELECT ALL", parent)
    selectionALL.triggered.connect(lambda: select_all(parent))
    menu.addAction(selectionALL)  # Correção aqui!

    # Botão "CLOSE"
    close_conetion = QAction("CLOSE CONETION", parent)
    close_conetion.triggered.connect(lambda: close(parent))
    menu.addAction(close_conetion)

def close(parent):
    if hasattr(parent, 'db') and parent.db is not None:
        parent.db.close_conection()

def select_all(parent):
    if hasattr(parent, 'db') and parent.db is not None:
        parent.db.select_all()
