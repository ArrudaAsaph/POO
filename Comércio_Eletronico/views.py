from models.class_Categoria import Categoria, Categorias
from models.class_Cliente import Cliente, Clientes
from models.class_Produto import Produto, Produtos
from models.class_Vendas import Venda, Vendas
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
    

#=====================================================================================
# CRIAR ADMIN

    @staticmethod
    def cliente_Admin():
        for c in Views.listar_Clientes():
            if c.email == "admin@gmail.com":
                return None

        admin = Cliente(0,"admin","0000","admin@gmail.com","admin123")
        Clientes.inserir_Clien(admin)

# AUTENTIFCAR CLIENTE

    @staticmethod
    def Autentificar_Cliente(email,senha):
        for c in Views.listar_Clientes():
            if (email == "admin@gmail.com"):
                if (c.email == email and c.senha == senha):
                    return {"id": c.id, "nome": c.nome}, "admin"
            else:
                if (c.email == email and c.senha == senha):
                    return {"id": c.id, "nome": c.nome}, "usuario"
        return None, None
    

#=====================================================================================
# PRODUTOS

    @staticmethod
    def reajuste_Todos(porcentagem):
        for c in Views.listar_Produto():
            Views.atualizar_Produto(c.id,c.descricao,(c.preco * (1 + porcentagem)),c.estoque,c.id_Categoria)
    
    @staticmethod
    def reajuste_Todos(id,porcentagem):
        c = Produtos.listar_Id(id)
        for c in Views.listar_Produto():
            Views.atualizar_Produto(c.id,c.descricao,(c.preco * (1 + porcentagem)),c.estoque,c.id_Categoria)
    
    @staticmethod
    def inserir_Venda(carrinho,valor,id_Cliente):
        ativo = False
        for venda in Vendas.lista_Vend():
            # self, id, data, carrinho, total, id_Cliente
            if venda.id_Cliente == id_Cliente and venda.carrinho == True:
                ativo = True
                break
            if (ativo == False):
                nova_Venda = Venda(0,None,carrinho,valor,id_Cliente)
                Vendas.inseri_Vend(nova_Venda)
    
    @staticmethod
    def Fechar_Venda(id_Cliente):
        id_venda = 0
        for venda in Vendas.lista_Vend():
            if venda.id_Cliente == id_Cliente and venda.carrinho == True:
                id_venda = venda.id
                id = venda.id
                carrinho = False
                total = venda.total
                id_cliente = venda.id_Cliente
                data = venda.data
                v = Venda(id,data,carrinho,total,id_Cliente)
                Vendas.atualiza_Vend(v)
