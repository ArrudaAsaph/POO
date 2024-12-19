from models.class_Categoria import Categoria, Categorias
from models.class_Cliente import Cliente, Clientes
from models.class_Produto import Produto, Produtos
from models.class_Vendas import Venda, Vendas
from models.class_VendaItens import VendaItem, VendasItems
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
    def autentificar_Cliente(email,senha):
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
            Views.atualizar_Produto(c.id,c.descricao,(c.preco * (1 + porcentagem)),c.estoque,c.id_categoria)
    
    @staticmethod
    def reajuste_Unico(id,porcentagem):
        c = Produtos.listar_Id(id)
        
        Views.atualizar_Produto(c.id,c.descricao,(c.preco * (1 + porcentagem)),c.estoque,c.id_categoria)
#=====================================================================================
# VENDA 
    @staticmethod
    def inserir_Venda(carrinho, total, id_cliente):
        ativo = False
        for venda in Vendas.listar_Vend():
            if venda.id_Cliente == id_cliente and venda.carrinho == True:
                ativo = True
                break
        if ativo == False:
            nova_venda = Venda(0, None, carrinho, total, id_cliente)
            Vendas.inserir_Vend(nova_venda)

    @staticmethod
    def fechar_Venda(id_cliente):
        id_venda = 0
        for venda in Vendas.listar_Vend():
            # id, data, carrinho, total, id_Cliente

            if venda.id_Cliente == id_cliente and venda.getCarrinho == True:
                id_venda = venda.id
                id = venda.id
                carrinho = False
                total = venda.total
                id_cliente = venda.id_Cliente
                data = venda.data
                venda_atualizada = Venda(id, data, carrinho, total, id_cliente)
                Vendas.atualizar_Vend(venda_atualizada)
                break
        
        for vendaitem in VendasItems.listar_VendaIt():
            # id, nome, qtd, preco, id_venda, id_produto
            id_produto = 0
            if vendaitem.id_venda == id_venda:
                id_produto = vendaitem.id_produto

            for produto in Produtos.listar_Prod():
                if produto.id == id_produto:
                    estoque = produto.estoque
                    estoque = estoque + vendaitem.qtd
                    Views.atualizar_Produto(produto.id,  produto.descricao, produto.preco, estoque, produto.id_categoria)
                    break

    @staticmethod
    def listar_Venda():
        return Vendas.listar_Vend()
    
    @staticmethod
    def atualizar_Venda(id, data, carrinho, total, id_cliente):
        venda_atualizada = Venda(id, data, carrinho, total, id_cliente)
        Vendas.atualizar_Vend(venda_atualizada)



#=====================================================================================
# VENDA ITEM
    @staticmethod
    def adicionar_VendaItem(nome, quantidade, preco, id_venda, id_produto):
        nova_VendaItem = VendaItem(0, nome, quantidade, preco, id_venda, id_produto)
        VendasItems.inserir_VendaItem(nova_VendaItem)

    @staticmethod
    def listar_VendaItem():
        return VendasItems.listar_VendaItem() 
    
    @staticmethod
    def atualizar_VendaItem(id, nome, quantidade, preco, id_venda, id_produto):
    #    id, nome, qtd, preco, id_venda, id_produto
        venda_atualizada = VendaItem(0, nome, quantidade, preco, id_venda, id_produto)
        VendasItems.atualizar_VendaItem(venda_atualizada)

    @staticmethod
    def excluir_VendaItem(id):
        v = VendaItem(id, " ", 0, 0, None, None)
    #    id, nome, qtd, preco, id_venda, id_produto

        VendasItems.excluir_VendaItem(v)
# adicionar_VendaItem(nome, quantidade, preco, id_venda, id_produto):
Views.adicionar_VendaItem("asaph",4,60,10,2)
print("olá")
