from application.model.entity.Produto import Produto 
from application import listaEstatua

class ProdutoDAO:
    def __init__(self):
        self._listaEstatua = listaEstatua 

    def listar_produtos(self):
        return self._listaEstatua

    def buscar_por_id(self, id):
        for produto in range(0, len(self._listaEstatua)):
            if self._listaEstatua[produto].get_id() == int(id):
                return self._listaEstatua[produto]
        return None 
        

