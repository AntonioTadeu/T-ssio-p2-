from flask import render_template, request
from application import app
from application.model.entity.Produto import Produto
from application.model.dao.produto_dao import ProdutoDAO


@app.route ('/')
def home():
    produto_dao = ProdutoDAO()    
    produto_lista = produto_dao.buscar_todos()
    return render_template("index.html", listaProdutos = produto_lista)
