class Produto:
    def __init__(self, nome, descricao=None, preco=0.0, estoque=0):
        """
        Modelo de Produto.

        :param nome: Nome do produto (obrigatório).
        :param descricao: Descrição opcional do produto.
        :param preco: Preço do produto (padrão: 0.0).
        :param estoque: Quantidade em estoque (padrão: 0).
        """
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        """Retorna uma representação textual do produto."""
        return f"Produto(nome={self.nome}, descricao={self.descricao}, preco={self.preco}, estoque={self.estoque})"

    def to_dict(self):
        """Retorna o produto como um dicionário, útil para conversões JSON ou manipulação em APIs."""
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque
        }