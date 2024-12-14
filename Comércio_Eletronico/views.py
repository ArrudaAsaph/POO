from models.class_Categoria import Categoria, Categorias
from models.class_Cliente import Cliente, Clientes
from models.class_Produto import Produto, Produtos

class Views:
    
    def adicionar_Cliente(nome,telefone,email,senha):
        novo_Cliente = Cliente(0,nome,telefone,email,senha)
        Clientes.inserir_Clien(novo_Cliente)
