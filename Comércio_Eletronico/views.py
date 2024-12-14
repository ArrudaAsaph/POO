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

    @staticmethod
    def remover_Cliente(id):
        cliente_removido = Cliente(id,"","","","")
        Clientes.excluir_Clien(cliente_removido)
    

    @staticmethod
    def adicionar_Categoria(descricao):
        nova_Categoria = Categoria(0,descricao)
        Categorias.inserir_Categ(nova_Categoria)

    @staticmethod
    def listar_Categoria():
        return Categorias.listar_Categ()
    
    
    @staticmethod
    def atualizar_Categoria(id,descricao):
        categoria_atualizado = Categoria(id,descricao)
        return Categorias.atualizar_Categ(categoria_atualizado)

    @staticmethod
    def remover_Categoria(id):
        categoria_removido = Categoria(id,"")
        Categorias.excluir_Categ(categoria_removido)
    
    @staticmethod
    def adicionar_Produto(descricao,preco,quantidade,id_Categoria):
        novo_Produto = Produto(0,descricao,preco,quantidade,id_Categoria)
        Produtos.inserir_Prod(novo_Produto)

    @staticmethod
    def listar_Produto():
        return Produtos.listar_Prod()
    
    @staticmethod
    def atualizar_Produto(id,descricao,preco,estoque,id_Categoria):
        produto_atualizado = Produto(id,descricao,preco,estoque,id_Categoria)
        Produtos.atualizar_Prod(produto_atualizado)
    
    @staticmethod
    def remover_Produto(id):
        produto_removido = Produto(id,"","","","")
        Produtos.excluir_Prod(produto_removido)
