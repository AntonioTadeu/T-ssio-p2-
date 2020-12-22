class Produto:

    def __init__(self, id, nome, descricao, precoOficial, precoLancamento, parcelamento):
        self._id = id 
        self._nome = nome
        self._descricao = descricao
        self._precoOficial = precoOficial
        self._precoLancamento = precoLancamento 
        self._parcelamento = parcelamento 

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_precoOficial(self):
        return self._precoOficial

    def get_precoLancamento(self):
        return self._precoLancamento

    def get_parcelamento(self):
        return self._parcelamento




