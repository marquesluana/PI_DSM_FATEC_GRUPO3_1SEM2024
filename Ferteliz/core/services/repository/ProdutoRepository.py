from ..connection import get_db

class ProductModel:
    def __init__(self, dataVenda, codigoVenda, codigoCliente, codigoFornecedor, nomeProduto, descricaoProduto, quantidade, valorUnitario, valorTotal ):
        self.dataVenda = dataVenda
        self.codigoVenda = codigoVenda
        self.codigoCliente = codigoCliente
        self.codigoFornecedor = codigoFornecedor
        self.nomeProduto = nomeProduto
        self.descricaoProduto = descricaoProduto
        self.quantidade = quantidade
        self.valorUnitario = valorUnitario
        self.valorTotal = valorTotal

    def save(self):
        db = get_db()
        product_data = {
            "dataVenda": self.dataVenda,
            "codigoVenda": self.codigoVenda,
            "codigoCliente": self.codigoCliente,
            "codigoFornecedor": self.codigoFornecedor,
            "nomeProduto": self.nomeProduto,
            "descricaoProduto": self.descricaoProduto,
            "quantidade": self.quantidade,
            "valorUnitario": self.valorUnitario,
            "valorTotal": self.valorTotal
        }
        db.products.insert_one(product_data)

    @staticmethod
    def find_by_name(nomeProduto):
        db = get_db()
        return db.products.find_one({"nomeProduto": nomeProduto})