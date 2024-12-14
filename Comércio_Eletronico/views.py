from models.class_Categoria import Categoria, Categorias
from models.class_Cliente import Cliente, Clientes
from models.class_Produto import Produto, Produtos

class Views:
    @staticmethod
    def adicionar_Cliente(nome,telefone,email,senha):
        novo_Cliente = Cliente(0,nome,telefone,email,senha)
        Clientes.inserir_Clien(novo_Cliente)

    @staticmethod
    def listar_Clientes():
        return Clientes.listar_Clien()
    
    @staticmethod
    def atualizar_Cliente(id,nome,telefone,email,senha):
        cliente_atualizado = Cliente(id,nome,telefone,email,senha)
        return Clientes.atualizar_Clien(cliente_atualizado)