class Produto:

    def __init__(self, id, imagemProduto,  nome, descricao, precoOficial, precoLancamento, valorParcela, numeroParcelas):
        self._id = id 
        self._imagemProduto = imagemProduto
        self._nome = nome
        self._descricao = descricao
        self._precoOficial = precoOficial
        self._precoLancamento = precoLancamento 
        self._valorParcela = valorParcela
        self._numeroParcelas = numeroParcelas

    def get_id(self):
        return self._id

    def get_imagemProduto(self):
        return self._imagemProduto

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_precoOficial(self):
        return self._precoOficial

    def get_precoLancamento(self):
        return self._precoLancamento

    def get_valorParcela(self):
        return self._valorParcela

    def get_numeroParcelas(self):
        return self._numeroParcelas






