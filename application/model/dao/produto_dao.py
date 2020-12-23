from application.model.entity.Produto import Produto
import json 



class ProdutoDAO:
    def __init__(self):
        self._produto_list=[]         

    def buscar_todos(self):
        with open('C:\\Users\\anton\\Desktop\\trabalho p1\\T-ssio-p2-\\products.json') as product_file:
            product_list = json.load(product_file)
        for product in product_list:
            self._produto_list.append(Produto(product['id'], product['image'], product['name'], product['description'], product['oldPrice'], product['price'], product['installments']['value'], product['installments']["count"]))
        return self._produto_list
        


       

   

