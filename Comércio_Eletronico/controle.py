from views import Views

class Controle:
    @classmethod
    def Cliente_Validation(cls,nome,telefone,email,senha):
        Views.cliente_Admin()
        Views.adicionar_Cliente(nome,telefone,email,senha)
    #8498143
    @classmethod
    def Cliente_Validation_Name(cls,nome):
        nome = nome.split()
        print(nome)
        space = " "
        for name in nome:
            name = name.capitalize()
            if (name == nome[0].capitalize()):
                upperName = name
                
                upperName += space
            else:
                upperName += name
                upperName += space
        return upperName
    
    @classmethod
    def Cliente_Validation_Email(cls,email):
        if ('@' in email): 
            return email
        else:   
            ValueError("Número inválido!")
            return None

    @classmethod
    def Cliente_Validation_Phone(cls,telefone):
        if (len(telefone) > 15 or len(telefone) < 11 ):
            ValueError("Número inválido!")
            return None
        else:
            number = "("
            parenthenses = ")"
            for i in range(1,len(telefone)):
                if (i == 1):
                    number += telefone[i-1]
                    number += telefone[i]
                    number += parenthenses
                    number += " "
                elif (i == 7) :
                    number += "-"
                    number += telefone[i]
                else:
                    number += telefone[i]
            return number

    @staticmethod
    def Cliente_Listar():
        return Views.listar_Clientes()
    
    @staticmethod
    def Cliente_Atualizar(id,nome,telefone,email,senha):
        return Views.atualizar_Cliente(id,nome,telefone,email,senha)
    
    @staticmethod
    def Cliente_Excluir(id):
        return Views.remover_Cliente(id)
    
    @staticmethod
    def Categoria_Validation_Description(description):
        if len(description) > 3:
            description = description.capitalize()
            descricoes = Controle.Categoria_Listar()
            for descri in descricoes:
                if descri.descricao == description:
                    return
            return Views.adicionar_Categoria(description)
        else:
            return None

    @staticmethod
    def Categoria_Listar():
        return Views.listar_Categoria()
    
    @staticmethod
    def Categoria_Atualizar(id,descricao):
        return Views.atualizar_Categoria(id,descricao)

    @staticmethod
    def Categoria_Excluir(id):
        return Views.remover_Categoria(id)
    

    @staticmethod
    def Produto_Validation(descricao,preco,quantidade,idCategoria):
        Views.adicionar_Produto(descricao,preco,quantidade,idCategoria)

    @staticmethod 
    def Produto_Validation_IdCatogoria(idCategoria):
        lista_Categorias = Views.listar_Categoria()

        for categorias in lista_Categorias:
            print(f"categorias{categorias}")
            print(f"categorias ID{categorias.id}")

            print(f"Lista categorias{lista_Categorias}")

            if idCategoria == categorias.id: 
                return idCategoria
        ValueError("Categoria inválida!")
        return None
    
    @staticmethod
    def Produto_Listar():
        return Views.listar_Produto()
    
    @staticmethod
    def Produto_Atualizar(id,descricao,preco,estoque,id_Categoria):
        return Views.atualizar_Produto(id,descricao,preco,estoque,id_Categoria)


    @staticmethod
    def Produto_Excluir(id):
        return Views.remover_Produto(id)
    

    @staticmethod
    def Admin():
        return Views.cliente_Admin()
    
    @staticmethod
    def Autentification(email,senha):
        return Views.autentificar_Cliente(email,senha)
    
    @staticmethod
    def Reajustar_Produto_Unico(id,porcentagem):
        return Views.reajuste_Unico(id,porcentagem)

    @staticmethod
    def Rejustar_Todos(porcentagem):
        return Views.reajuste_Todos(porcentagem)
    
    @staticmethod
    def Adicionar_Venda(carrinho, total, id_cliente):
        return Views.inserir_Venda(carrinho, total, id_cliente)
    
    @staticmethod
    def Fechar_Venda(id_cliente):
        return Views.fechar_Venda(id_cliente)

    @staticmethod
    def Listar_Venda():
        return Views.listar_Venda()

    @staticmethod
    def Atualizar_Venda(id, data, carrinho, total, id_cliente):
        return Views.atualizar_Venda(id, data, carrinho, total, id_cliente)
    
    @staticmethod
    def Adicionar_VendaItem(nome, quantidade, preco, id_venda, id_produto):
        return Views.adicionar_VendaItem(nome, quantidade, preco, id_venda, id_produto)

    @staticmethod
    def Listar_VendaItem():
        return Views.listar_VendaItem()

    @staticmethod
    def Atualizar_VendaItem(id,nome, quantidade, preco, id_venda, id_produto):
        return Views.atualizar_VendaItem(id,nome, quantidade, preco, id_venda, id_produto)
    
    @staticmethod
    def Excluir_VendaItem(id):
        return Views.excluir_VendaItem(id)

